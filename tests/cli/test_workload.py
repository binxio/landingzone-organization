from unittest.mock import patch, mock_open

from click.testing import CliRunner

from landingzone_organization import Organization
from landingzone_organization.cli import cli


def test_workload() -> None:
    runner = CliRunner()
    result = runner.invoke(cli, ["workload"])

    assert result.exit_code == 0


def test_workload_list(organization: Organization) -> None:
    runner = CliRunner()

    with patch(
        "landingzone_organization.cli.context.open",
        mock_open(read_data=organization.dump()),
    ):
        result = runner.invoke(cli, ["workload", "list"])

    assert result.exit_code == 0
