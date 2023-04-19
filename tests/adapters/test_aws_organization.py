from botocore.stub import Stubber

from landingzone_organization.adapters import AWSOrganization


def test_simple_read() -> None:
    adapter = AWSOrganization()

    with Stubber(adapter._AWSOrganization__client) as stubber:
        stubber.add_response(
            "list_roots", {"Roots": [{"Id": "r-1234"}]}, {"MaxResults": 1}
        )
        stubber.add_response(
            "list_children",
            {
                "Children": [
                    {"Id": "111111111111", "Type": "ACCOUNT"},  # mpa account
                ]
            },
            {"ChildType": "ACCOUNT", "ParentId": "r-1234"},
        )
        stubber.add_response(
            "list_children",
            {
                "Children": [
                    {"Id": "ou-1", "Type": "ORGANIZATIONAL_UNIT"},  # Core OU
                    {"Id": "ou-2", "Type": "ORGANIZATIONAL_UNIT"},  # Security OU
                    {"Id": "ou-3", "Type": "ORGANIZATIONAL_UNIT"},  # Workload OU
                ]
            },
            {"ChildType": "ORGANIZATIONAL_UNIT", "ParentId": "r-1234"},
        )
        stubber.add_response(
            "describe_account",
            {
                "Account": {
                    "Id": "111111111111",
                    "Name": "xebia-mpa",
                }
            },
            {"AccountId": "111111111111"},
        )
        stubber.add_response(
            "describe_organizational_unit",
            {
                "OrganizationalUnit": {
                    "Id": "ou-1",
                    "Name": "Core",
                }
            },
            {"OrganizationalUnitId": "ou-1"},
        )
        stubber.add_response(
            "list_children",
            {
                "Children": [
                    {"Id": "222222222222", "Type": "ACCOUNT"},  # network
                ]
            },
            {"ChildType": "ACCOUNT", "ParentId": "ou-1"},
        )
        stubber.add_response(
            "list_children",
            {"Children": []},
            {"ChildType": "ORGANIZATIONAL_UNIT", "ParentId": "ou-1"},
        )
        stubber.add_response(
            "describe_account",
            {
                "Account": {
                    "Id": "222222222222",
                    "Name": "xebia-network",
                }
            },
            {"AccountId": "222222222222"},
        )
        stubber.add_response(
            "describe_organizational_unit",
            {
                "OrganizationalUnit": {
                    "Id": "ou-2",
                    "Name": "Security",
                }
            },
            {"OrganizationalUnitId": "ou-2"},
        )
        stubber.add_response(
            "list_children",
            {
                "Children": [
                    {"Id": "333333333333", "Type": "ACCOUNT"},  # audit
                ]
            },
            {"ChildType": "ACCOUNT", "ParentId": "ou-2"},
        )
        stubber.add_response(
            "list_children",
            {"Children": []},
            {"ChildType": "ORGANIZATIONAL_UNIT", "ParentId": "ou-2"},
        )
        stubber.add_response(
            "describe_account",
            {
                "Account": {
                    "Id": "333333333333",
                    "Name": "xebia-audit",
                }
            },
            {"AccountId": "333333333333"},
        )

        stubber.add_response(
            "describe_organizational_unit",
            {
                "OrganizationalUnit": {
                    "Id": "ou-3",
                    "Name": "Workload",
                }
            },
            {"OrganizationalUnitId": "ou-3"},
        )
        stubber.add_response(
            "list_children",
            {
                "Children": [
                    {"Id": "444444444444", "Type": "ACCOUNT"},  # workload
                ]
            },
            {"ChildType": "ACCOUNT", "ParentId": "ou-3"},
        )
        stubber.add_response(
            "list_children",
            {"Children": []},
            {"ChildType": "ORGANIZATIONAL_UNIT", "ParentId": "ou-3"},
        )
        stubber.add_response(
            "describe_account",
            {
                "Account": {
                    "Id": "444444444444",
                    "Name": "xebia-workload-development",
                }
            },
            {"AccountId": "444444444444"},
        )
        organization = adapter.parse()
        stubber.assert_no_pending_responses()

    assert (
        organization.by_account_id("444444444444").name == "xebia-workload-development"
    )
    assert organization.by_account_id("333333333333").name == "xebia-audit"
    assert organization.by_account_id("222222222222").name == "xebia-network"
    # assert organization.by_account_id("111111111111").name == "xebia-mpa"
