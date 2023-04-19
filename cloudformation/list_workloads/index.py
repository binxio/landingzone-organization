from typing import List
import json
import boto3
from landingzone_organization import Organization

client = boto3.client("sts")


def handler(event, context) -> List[str]:
    organization = Organization.load(json.dumps(event))
    workloads = organization.workloads(["Workload"])
    result = []

    for workload in workloads:
        result.append(workload.name)

    return result
