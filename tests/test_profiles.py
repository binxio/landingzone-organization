from unittest.mock import patch, mock_open, MagicMock

import boto3
import botocore

from landingzone_organization import Profiles

SAMPLE_AWS_CONFIG_FILE = """
[profile test-workload1-development]
sso_role_name = my-sso-audit-role

[profile test-workload1-testing]
sso_role_name = my-sso-audit-role

[profile test-workload1-acceptance]
sso_role_name = my-sso-audit-role

[profile test-workload1-production]
sso_role_name = my-sso-audit-role
"""


def mock_session() -> MagicMock:
    session = MagicMock()
    client = MagicMock()
    client.get_secret_value.return_value = {"SecretString": "my-secret"}
    session.client.return_value = client
    return session


@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data=SAMPLE_AWS_CONFIG_FILE,
)
@patch("boto3.session.Session", return_value=mock_session())
def test_multiple_profiles_and_regions(mock_session, mock_file) -> None:
    expected_regions = [
        # test-workload1-development will be called for:
        "eu-west-1",
        "eu-central-1",
        # test-workload1-testing will be called for:
        "eu-west-1",
        "eu-central-1",
        # test-workload1-acceptance will be called for:
        "eu-west-1",
        "eu-central-1",
        # test-workload1-production will be called for:
        "eu-west-1",
        "eu-central-1",
    ]
    executor = Profiles("/some/path/does/not/matter/mocked/anyway")

    def callback(session: boto3.session.Session, region: str) -> None:
        assert mock_session.return_value == session
        assert region == expected_regions.pop(0)

    executor.execute(["eu-west-1", "eu-central-1"], callback)


@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data=SAMPLE_AWS_CONFIG_FILE,
)
@patch("boto3.session.Session", return_value=mock_session())
def test_multiple_profiles_exceptions(mock_session, mock_file) -> None:
    executor = Profiles("/some/path/does/not/matter/mocked/anyway")

    def callback(session: boto3.session.Session, region: str) -> None:
        assert mock_session.return_value == session
        assert region == "eu-west-1"

        raise botocore.exceptions.ClientError(
            operation_name=MagicMock(), error_response=MagicMock()
        )

    executor.execute(["eu-west-1"], callback)

    assert "test-workload1-development-eu-west-1" in executor.client_exceptions
    assert "test-workload1-testing-eu-west-1" in executor.client_exceptions
    assert "test-workload1-acceptance-eu-west-1" in executor.client_exceptions
    assert "test-workload1-production-eu-west-1" in executor.client_exceptions
