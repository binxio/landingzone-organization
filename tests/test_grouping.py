from landingzone_organization import Organization


def test_workloads(organization: Organization) -> None:
    workloads = organization.workloads(["Workloads"])
    assert workloads.environments == {"development",
        "testing",
        "acceptance",
        "production"}

    assert len(workloads) == 4
    assert workloads.names == {"workload-1", "workload-2", "workload-3", "workload-4"}

    workload1 = workloads.by_name("workload-1")
    assert len(workload1.accounts) == 4
    assert workload1.environments == ["development",
        "testing",
        "acceptance",
        "production"]
    assert workload1.by_environment("development").name == "test-workload-1-development"
    assert workload1.by_environment("testing").name == "test-workload-1-testing"
    assert workload1.by_environment("acceptance").name == "test-workload-1-acceptance"
    assert workload1.by_environment("production").name == "test-workload-1-production"

    workload2 = workloads.by_name("workload-2")
    assert len(workload2.accounts) == 3
    assert workload2.environments == ["development", "testing", "acceptance"]
    assert workload2.by_environment("development").name == "test-workload-2-development"
    assert workload2.by_environment("testing").name == "test-workload-2-testing"
    assert workload2.by_environment("acceptance").name == "test-workload-2-acceptance"
    assert workload2.by_environment("production") is None

    workload3 = workloads.by_name("workload-3")
    assert len(workload3.accounts) == 2
    assert workload3.environments == ["development", "testing"]
    assert workload3.by_environment("development").name == "test-workload-3-development"
    assert workload3.by_environment("testing").name == "test-workload-3-testing"
    assert workload3.by_environment("acceptance") is None
    assert workload3.by_environment("production") is None

    workload4 = workloads.by_name("workload-4")
    assert len(workload4.accounts) == 1
    assert workload4.environments == ["development"]
    assert workload4.by_environment("development").name == "test-workload-4-development"
    assert workload4.by_environment("testing") is None
    assert workload4.by_environment("acceptance") is None
    assert workload4.by_environment("production") is None


def test_workloads_iteration(organization: Organization) -> None:
    workloads = organization.workloads(["Workloads"])

    for workload in workloads:
        assert len(workload.accounts) > 0
