import json
import boto3
from landingzone_organization import AWSOrganization

client = boto3.client("sts")


def handler(event, context) -> dict:
    organization = AWSOrganization().parse()
    return json.loads(organization.dump())
