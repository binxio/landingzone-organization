from landingzone_organization import Organization


def test_export(organization: Organization) -> None:
    frozen = organization.dump()
    imported_organization = Organization.load(frozen)
    assert organization == imported_organization
