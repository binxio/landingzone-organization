def test_workload_environment_order(organization) -> None:
    workload = organization.workloads(["Workloads"]).by_name("workload-1")
    assert [
        "development",
        "testing",
        "acceptance",
        "production",
    ] == workload.environments
