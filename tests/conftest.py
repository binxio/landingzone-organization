import os
import pytest

from landingzone_organization import (
    Account,
    Group,
    Groups,
    Organization,
    OrganizationUnit,
    Workload
)


@pytest.fixture
def config_path() -> str:
    return os.path.join(os.path.dirname(__file__), "workloads")


@pytest.fixture
def groups(organization) -> Groups:
    return Groups(
        groups=[
            Group("Core", "eu-west-1", ["Core"]),
            Group("Security", "eu-west-1", ["Security"]),
            Group("Development", "eu-west-1", ["Workloads", "Development"]),
            Group("Testing", "eu-west-1", ["Workloads", "Testing"]),
            Group("Acceptance", "eu-west-1", ["Workloads", "Acceptance"]),
            Group("Production", "eu-west-1", ["Workloads", "Production"]),
        ],
        organization=organization,
    )


@pytest.fixture
def workload(organization) -> Workload:
    return organization.workloads(["Workloads"]).by_name("workload-1")


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
