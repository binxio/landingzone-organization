---
title: "Using AWS Lambda"
weight: 2
chapter: true
pre: "<b>2. </b>"
---

# Using AWS Lambda

You can also use this module within an AWS Lambda function. AWS recommends to not use the master payer account for
anything other than providing AWS Organizations and billing. But in order to query the AWS Organization we need a role
in the master payer account that we can assume. In [`cloudformation/prerequisites.yaml`](https://github.com/binxio/landingzone-organization/blob/main/cloudformation/prerequisites.yaml)
you can see how you can create a role that can be assumed from another account.

You can than assume that role from any other account and initialize the module with accurate organization information.

See: [`cloudformation/read_organization/index.py`](https://github.com/binxio/landingzone-organization/blob/main/cloudformation/read_organization/index.py)