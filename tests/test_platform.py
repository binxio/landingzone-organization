from landingzone_organization import Organization


def test_platform_accounts(organization: Organization) -> None:
    platform_accounts = set(
        map(lambda account: account.name, organization.platform_accounts)
    )

    assert platform_accounts == {"root-account", "connectivity", "audit"}
