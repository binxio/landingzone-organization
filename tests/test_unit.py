from landingzone_organization import Groups, Organization


def test_security_and_core_ou(organization: Organization) -> None:
    assert organization.by_name("Security").has_accounts is True
    assert len(organization.by_name("Security").accounts) == 1
    assert organization.by_name("Core").has_accounts is True
    assert len(organization.by_name("Core").accounts) == 1


def test_workload_ou(organization: Organization) -> None:
    workloads = organization.by_name("Workloads")
    assert workloads.has_accounts is False

    assert len(workloads.accounts_recursive) == 10
    assert workloads.by_name("Development").has_accounts is True
    assert len(workloads.by_name("Development").accounts) == 4
    assert workloads.by_name("Testing").has_accounts is True
    assert len(workloads.by_name("Testing").accounts) == 3
    assert workloads.by_name("Acceptance").has_accounts is True
    assert len(workloads.by_name("Acceptance").accounts) == 2
    assert workloads.by_name("Production").has_accounts is True
    assert len(workloads.by_name("Production").accounts) == 1


def test_resolve_accounts_based_on_security_unit(groups: Groups) -> None:
    accounts = groups.by_name("Security").accounts
    assert len(accounts) == 1
    assert accounts[0].name == "audit"


def test_resolve_accounts_based_on_core_unit(groups: Groups) -> None:
    accounts = groups.by_name("Core").accounts
    assert len(accounts) == 1
    assert accounts[0].name == "connectivity"


def test_resolve_accounts_based_on_workload_development(groups: Groups) -> None:
    accounts = groups.by_name("Development").accounts
    assert len(accounts) == 4
    assert accounts[0].name == "test-workload-1-development"
    assert accounts[1].name == "test-workload-2-development"
    assert accounts[2].name == "test-workload-3-development"
    assert accounts[3].name == "test-workload-4-development"


def test_resolve_accounts_based_on_workload_testing(groups: Groups) -> None:
    accounts = groups.by_name("Testing").accounts
    assert len(accounts) == 3
    assert accounts[0].name == "test-workload-1-testing"
    assert accounts[1].name == "test-workload-2-testing"
    assert accounts[2].name == "test-workload-3-testing"


def test_resolve_accounts_based_on_workload_acceptance(groups: Groups) -> None:
    accounts = groups.by_name("Acceptance").accounts
    assert len(accounts) == 2
    assert accounts[0].name == "test-workload-1-acceptance"
    assert accounts[1].name == "test-workload-2-acceptance"


def test_resolve_accounts_based_on_workload_production(groups: Groups) -> None:
    accounts = groups.by_name("Production").accounts
    assert len(accounts) == 1
    assert accounts[0].name == "test-workload-1-production"
