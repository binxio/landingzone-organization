import os
from unittest.mock import patch, mock_open

from click.testing import CliRunner

from landingzone_organization import Organization
from landingzone_organization.cli import cli


@patch("landingzone_organization.workload_generator.WorkloadGenerator")
@patch("boto3.session.Session")
def test_export_workloads(
    mock_session, mock_workload_generator, organization: Organization
) -> None:
    with patch(
        "landingzone_organization.cli.context.open",
        mock_open(read_data=organization.dump()),
    ):
        config_path = os.path.join(os.path.dirname(__file__), "workloads")
        runner = CliRunner()
        result = runner.invoke(cli, ["export", "workloads", config_path, "Workloads"])

    assert mock_workload_generator.return_value.execute.called is True
    assert result.exit_code == 0
