from unittest.mock import patch, mock_open

from click.testing import CliRunner

from landingzone_organization import Organization
from landingzone_organization.cli import cli


def test_profiles() -> None:
    runner = CliRunner()
    result = runner.invoke(cli, ["profiles"])
    assert result.exit_code == 0


def test_profiles_generate_no_organization_name(organization: Organization) -> None:
    runner = CliRunner()
    result = runner.invoke(cli, ["profiles", "generate"])
    assert result.exit_code == 2


def test_profiles_generate(organization: Organization) -> None:
    runner = CliRunner()
    result = runner.invoke(
        cli,
        [
            "profiles",
            "generate",
            "acme",
            "--sso-start-url",
            "https://acme.awsapps.com/start",
            "--sso-region",
            "eu-central-1",
            "--role-session-name",
            "John.Doe@acme.com",
            "--sso-role-name",
            "my-sso-audit-role",
        ],
    )
    assert result.exit_code == 0
