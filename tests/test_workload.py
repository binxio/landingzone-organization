from landingzone_organization import Workload


def test_workload_environment_order(organization) -> None:
    workload = organization.workloads(["Workloads"]).by_name("workload-1")
    assert [
        "development",
        "testing",
        "acceptance",
        "production",
    ] == workload.environments


def test_load_workload_simple_by_dict() -> None:
    workload = Workload.from_dict({"Name": "my-workload"}, [])
    assert workload.name == "my-workload"
    assert workload.display_name is None


def test_load_workload_by_dict() -> None:
    workload = Workload.from_dict(
        {"Name": "my-workload", "DisplayName": "My Workload"}, []
    )
    assert workload.name == "my-workload"
    assert workload.display_name == "My Workload"
