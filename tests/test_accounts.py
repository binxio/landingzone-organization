from landingzone_organization import Organization


def test_resolve_accounts_based_on_account_ids(organization: Organization) -> None:
    assert organization.by_account_id("999999999999") is None
    assert organization.by_account_id("111111111111").name == "connectivity"
    assert organization.by_account_id("111111111112").name == "audit"
    assert (
        organization.by_account_id("555511111111").name == "test-workload-1-production"
    )
