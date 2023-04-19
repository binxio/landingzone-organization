from click.testing import CliRunner
from landingzone_organization.cli import cli


def test_entrypoint() -> None:
    runner = CliRunner()
    result = runner.invoke(cli)

    assert result.exit_code == 0
