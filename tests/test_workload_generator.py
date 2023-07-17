from unittest.mock import mock_open, patch, call

from landingzone_organization.workload import Workload
from landingzone_organization.workload_generator import WorkloadGenerator


@patch("os.path.isfile")
@patch("os.path.isdir")
@patch("os.mkdir")
@patch("builtins.open", new_callable=mock_open)
def test_generate_new_workload(
    mock_file, mock_mkdir, mock_isdir, mock_isfile, config_path: str, workload: Workload
) -> None:
    mock_isdir.return_value = False
    mock_isfile.return_value = False
    mock_file.return_value.write.return_value = None
    generator = WorkloadGenerator(config_path=config_path, workload=workload)
    generator.execute()

    assert mock_mkdir.called is True

    assert mock_file.call_args_list == [
        call(f"{config_path}/workload-1/info.yaml", "w"),
        call(f"{config_path}/workload-1/development.yaml", "w"),
        call(f"{config_path}/workload-1/testing.yaml", "w"),
        call(f"{config_path}/workload-1/acceptance.yaml", "w"),
        call(f"{config_path}/workload-1/production.yaml", "w"),
    ]


@patch("os.path.isfile")
@patch("os.path.isdir")
@patch("os.mkdir")
@patch("builtins.open", new_callable=mock_open)
def test_generate_existing_workload(
    mock_file, mock_mkdir, mock_isdir, mock_isfile, config_path: str, workload: Workload
) -> None:
    mock_isdir.return_value = True
    mock_isfile.return_value = True
    mock_file.return_value.write.return_value = None

    generator = WorkloadGenerator(config_path=config_path, workload=workload)

    with patch("yaml.safe_load") as mock_load:
        mock_load.return_value = {"Name": "workload-1"}
        generator.execute()

    assert mock_mkdir.called is False

    assert mock_file().write.call_args_list == [
        call("Name"),
        call(":"),
        call(" "),
        call("workload-1"),
        call("\n"),
        call("Environments"),
        call(":"),
        call("\n"),
        call("-"),
        call(" "),
        call("development"),
        call("\n"),
        call("-"),
        call(" "),
        call("testing"),
        call("\n"),
        call("-"),
        call(" "),
        call("acceptance"),
        call("\n"),
        call("-"),
        call(" "),
        call("production"),
        call("\n"),
    ]
    assert mock_file.call_args_list == [
        call(f"{config_path}/workload-1/info.yaml", "r"),
        call(f"{config_path}/workload-1/info.yaml", "w"),
        call(),
    ]


@patch("os.path.isfile")
@patch("os.path.isdir")
@patch("os.mkdir")
@patch("builtins.open", new_callable=mock_open)
def test_generate_existing_workload_new_name(
    mock_file, mock_mkdir, mock_isdir, mock_isfile, config_path: str, workload: Workload
) -> None:
    mock_isdir.return_value = True
    mock_isfile.return_value = True
    mock_file.return_value.write.return_value = None

    generator = WorkloadGenerator(config_path=config_path, workload=workload)

    with patch("yaml.safe_load") as mock_load:
        mock_load.return_value = {"Name": "old-workload"}
        generator.execute()

    assert mock_mkdir.called is False

    assert mock_file().write.call_args_list == [
        call("Name"),
        call(":"),
        call(" "),
        call("workload-1"),
        call("\n"),
        call("Environments"),
        call(":"),
        call("\n"),
        call("-"),
        call(" "),
        call("development"),
        call("\n"),
        call("-"),
        call(" "),
        call("testing"),
        call("\n"),
        call("-"),
        call(" "),
        call("acceptance"),
        call("\n"),
        call("-"),
        call(" "),
        call("production"),
        call("\n"),
    ]
    assert mock_file.call_args_list == [
        call(f"{config_path}/workload-1/info.yaml", "r"),
        call(f"{config_path}/workload-1/info.yaml", "w"),
        call(),
    ]
