---
title: "Using python tests"
weight: 4
chapter: true
pre: "<b>4. </b>"
---

# Using python tests

When you are using the module in your own python projects you may have a need to mock an organization structure. You can easily do this using pytest fixtures, you can add the following code to the `tests/conftest.py` file:  

```python
import pytest

from landingzone_organization import (
    Account,
    Organization,
    OrganizationUnit,
)


@pytest.fixture
def organization() -> Organization:
    return Organization(
        "r-1234",
        OrganizationUnit(
            id="r-1234",
            name="Root",
            accounts=[Account("root-account", "000000000000")],
            units=[
                OrganizationUnit(
                    id="ou-1",
                    name="Core",
                    accounts=[
                        Account("connectivity", "111111111111"),
                    ],
                ),
                OrganizationUnit(
                    id="ou-2",
                    name="Security",
                    accounts=[
                        Account("audit", "111111111112"),
                    ],
                ),
                OrganizationUnit(
                    id="ou-3",
                    name="Workloads",
                    accounts=[],
                    units=[
                        OrganizationUnit(
                            id="ou-4",
                            name="Development",
                            accounts=[
                                Account("test-workload-1-development", "22221111111"),
                                Account("test-workload-2-development", "22221111112"),
                                Account("test-workload-3-development", "22221111113"),
                                Account("test-workload-4-development", "22221111114"),
                            ],
                        ),
                        OrganizationUnit(
                            id="ou-5",
                            name="Testing",
                            accounts=[
                                Account("test-workload-1-testing", "333311111111"),
                                Account("test-workload-2-testing", "333311111112"),
                                Account("test-workload-3-testing", "333311111113"),
                            ],
                        ),
                        OrganizationUnit(
                            id="ou-6",
                            name="Acceptance",
                            accounts=[
                                Account("test-workload-1-acceptance", "444411111111"),
                                Account("test-workload-2-acceptance", "444411111112"),
                            ],
                        ),
                        OrganizationUnit(
                            id="ou-7",
                            name="Production",
                            accounts=[
                                Account("test-workload-1-production", "555511111111")
                            ],
                        ),
                    ],
                ),
                OrganizationUnit(
                    id="ou-8",
                    name="Sandbox",
                    accounts=[Account("test-001-sandbox", "999988887777")],
                ),
            ],
        ),
    )
```

Next you can create your tests in `tests/test_my_test_file.py` as followed:

```python
from landingzone_organization import Organization


def test_resolve_accounts_based_on_account_ids(organization: Organization) -> None:
    assert organization.by_account_id("999999999999") is None
    assert organization.by_account_id("111111111111").name == "connectivity"
    assert organization.by_account_id("111111111112").name == "audit"
    assert organization.by_account_id("555511111111").name == "test-workload-1-production"
```
