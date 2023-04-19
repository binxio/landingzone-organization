from landingzone_organization import Organization


def test_workloads_root(organization: Organization) -> None:
    workloads = organization.workloads([])

    assert workloads.names == {
        "workload-4",
        "workload-2",
        "workload-1",
        "workload-3",
        "001",
    }


def test_workloads_unknown_ou(organization: Organization) -> None:
    workloads = organization.workloads(["Sample"])

    assert workloads.names == set()


def test_workloads_workloads(organization: Organization) -> None:
    workloads = organization.workloads(["Workloads"])

    assert workloads.names == {"workload-4", "workload-2", "workload-1", "workload-3"}


def test_workloads_development(organization: Organization) -> None:
    workloads = organization.workloads(["Workloads", "Development"])
    assert workloads.names == {"workload-1", "workload-2", "workload-3", "workload-4"}


def test_workloads_testing(organization: Organization) -> None:
    workloads = organization.workloads(["Workloads", "Testing"])
    assert workloads.names == {"workload-1", "workload-2", "workload-3"}


def test_workloads_acceptance(organization: Organization) -> None:
    workloads = organization.workloads(["Workloads", "Acceptance"])
    assert workloads.names == {"workload-1", "workload-2"}


def test_workloads_production(organization: Organization) -> None:
    workloads = organization.workloads(["Workloads", "Production"])
    assert workloads.names == {"workload-1"}
