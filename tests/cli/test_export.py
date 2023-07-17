import os
from unittest.mock import patch

from click.testing import CliRunner

from landingzone_organization import Organization
from landingzone_organization.cli import cli


@patch("landingzone_organization.workload_generator.WorkloadGenerator")
@patch("landingzone_organization.AWSOrganization")
@patch("boto3.session.Session")
def test_prepare(
    mock_session, mock_organization, mock_workload_generator, organization: Organization
) -> None:
    mock_organization.return_value.parse.return_value = organization

    config_path = os.path.join(os.path.dirname(__file__), "workloads")
    runner = CliRunner()
    result = runner.invoke(cli, ["export", "workloads", config_path, "Workloads"])

    assert mock_workload_generator.return_value.execute.called is True

    assert result.exit_code == 0
