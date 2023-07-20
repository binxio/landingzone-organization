import pytest

from landingzone_organization import Organization, Workloads, Account
from landingzone_organization.schemas import (
    environment_resolver,
    InvalidSchemaException,
)


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


def test_workloads_resolve_non_matching_account_name(
    organization: Organization,
) -> None:
    workloads = organization.workloads(["Workloads", "Production"])
    workloads.resolve_account(Account(name="non_matching_name", account_id=""))
    assert workloads.names == {"workload-1"}


def test_load_by_path(workload_config_path: str) -> None:
    workloads = Workloads.load_by_path(workload_config_path, environment_resolver)

    assert workloads.names == {"example-workload"}
    assert workloads.environments == {
        "development",
        "testing",
        "acceptance",
        "production",
    }


def test_load_by_path_invalid(invalid_schema_config_path: str) -> None:
    with pytest.raises(InvalidSchemaException) as exc:
        Workloads.load_by_path(invalid_schema_config_path, environment_resolver)

    assert exc.value.message.startswith("Additional properties are not allowed") is True
