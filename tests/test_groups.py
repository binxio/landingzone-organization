from landingzone_organization import Groups, Group, Organization, Account


def test_group_names_are_valid(groups: Groups) -> None:
    assert groups.valid_group("Core") is True
    assert groups.valid_group("Security") is True
    assert groups.valid_group("Development") is True
    assert groups.valid_group("Testing") is True
    assert groups.valid_group("Acceptance") is True
    assert groups.valid_group("Production") is True
    assert groups.valid_group("core") is False
    assert groups.valid_group("security") is False
    assert groups.valid_group("development") is False
    assert groups.valid_group("testing") is False
    assert groups.valid_group("acceptance") is False
    assert groups.valid_group("production") is False
    assert groups.valid_group("NonExistingGroup") is False
    assert groups.valid_group("OtherNonExistingGroup") is False


def test_groups_without_organization() -> None:
    groups = Groups([Group("MyGroup", "eu-west-1", ["Workloads", "Development"])])
    assert groups.by_name("MyGroup").accounts == []


def test_unknown_group(groups: Groups) -> None:
    assert groups.by_name("UnknownGroup") is None


def test_unknown_ou_name(organization: Organization) -> None:
    group = Group("MyGroup", "eu-west-1", ["Workloads", "UnknownUnit"])
    group.organization(organization)

    assert group.accounts == []
