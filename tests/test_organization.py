from landingzone_organization import Organization


def test_all_accounts(organization: Organization) -> None:
    assert len(organization.accounts_recursive) == 14


def test_accounts(organization: Organization) -> None:
    assert len(organization.accounts([])) == 14
    assert len(organization.accounts(["Core"])) == 1
    assert len(organization.accounts(["Security"])) == 1
    assert len(organization.accounts(["Workloads"])) == 10
    assert len(organization.accounts(["Sandbox"])) == 1


def test_get_by_name(organization: Organization) -> None:
    workloads = organization.by_name("Workloads")
    assert workloads.name == "Workloads"
    assert workloads.by_name("Development").name == "Development"
    assert workloads.by_name("Testing").name == "Testing"
    assert workloads.by_name("Acceptance").name == "Acceptance"
    assert workloads.by_name("Production").name == "Production"
