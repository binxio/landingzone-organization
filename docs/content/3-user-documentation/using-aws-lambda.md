---
title: "Using AWS Lambda"
weight: 2
chapter: true
pre: "<b>2. </b>"
---

# Using AWS Lambda

> Please note, this needs to either be deployed in the master payer account of your organization. Or in a delegated administrator accounts.

You can also use this module within an AWS Lambda function. And those AWS Lambda functions can then be orchestrated using [Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html).

![Step Functions State Machine representation](/images/stepfunctions_graph.svg)

## State Machine

The definition of the state machine can be found here: [`cloudformation/state_machine.asl.json`](https://github.com/binxio/landingzone-organization/blob/main/cloudformation/state_machine.asl.json).

## Reading the organization

The first lambda will use the package to read the entire organization, the sample code can be found here: [`cloudformation/read_organization/index.py`](https://github.com/binxio/landingzone-organization/blob/main/cloudformation/read_organization/index.py).

## Using the data read

Next we can extract a list of workloads running within the organization, the sample code can be found here: [`cloudformation/list_workloads/index.py`](https://github.com/binxio/landingzone-organization/blob/main/cloudformation/list_workloads/index.py). 

## CloudFormation template

You can deploy the [`cloudformation/template.yaml`](https://github.com/binxio/landingzone-organization/blob/main/cloudformation/template.yaml) template using AWS SAM.
