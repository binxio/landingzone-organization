from click.testing import CliRunner
from unittest.mock import patch

from landingzone_organization import Organization
from landingzone_organization.cli import cli


@patch("landingzone_organization.adapters.AWSOrganization.parse")
def test_organization(mock_aws_organization, organization: Organization) -> None:
    mock_aws_organization.return_value = organization

    # TODO: Mock the write action
    runner = CliRunner()
    result = runner.invoke(cli, ["organization", "download"])

    assert result.exit_code == 0
