from unittest.mock import patch, mock_open
from click.testing import CliRunner

from landingzone_organization import Organization
from landingzone_organization.cli import cli
from landingzone_organization.cli.commands.account import perform_export


def test_account() -> None:
    runner = CliRunner()
    result = runner.invoke(cli, ["account"])

    assert result.exit_code == 0


def test_account_view(organization: Organization) -> None:
    runner = CliRunner()

    with patch(
        "landingzone_organization.cli.context.open",
        mock_open(read_data=organization.dump()),
    ):
        result = runner.invoke(cli, ["account", "view", "555511111111"])
        assert "555511111111" in result.output
        assert "test-workload-1-production" in result.output

    assert result.exit_code == 0


def test_account_view_unknown(organization: Organization) -> None:
    runner = CliRunner()

    with patch(
        "landingzone_organization.cli.context.open",
        mock_open(read_data=organization.dump()),
    ):
        result = runner.invoke(cli, ["account", "view", "100000000000"])
        assert "The 100000000000 is not known to this organization" in result.output

    assert result.exit_code == 0


def test_perform_export(organization: Organization) -> None:
    mock_file = mock_open()

    with patch("builtins.open", mock_file):
        perform_export("my-path.csv", organization.accounts([]))

    mock_file.assert_called_once_with('my-path.csv', 'w')
