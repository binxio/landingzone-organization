---
chapter: true
---

# landingzone-organization

This module allows you to query your landingzone organization. For example, if you want to know the names of all workloads that run in your AWS Cloud? You can use this module to fetch this information directly from the APIs from AWS.
## Getting started

Install and run the tests:

```shell
make install
make test
```

Check code complexity:

```shell
make complexity
```

Validate typing and formatting:

```shell
make lint
```

## Configuration

By default, this package does an assumption about your naming schema. It expects you use the following format:
`<PREFIX>-<WORKLOAD NAME>-<ENVIRONMENT>`. When you deviate from this schema you potentially need to provide 2 configuration
options. You can do this via 2 environment variable:

| **Name**                 | **Default Value** | **Description**                                                                                               |
|--------------------------|-------------------|---------------------------------------------------------------------------------------------------------------|
| PATTERN_WORKLOAD_NAME    | `.*?-(.*)-.*`     | The first match is used as the workload name.                                                                 |
| PATTERN_ENVIRONMENT_NAME | `.*-.*-(.*)`      | The first match is used as the environment name. For example: development, testing, acceptance or production. | 

### AWS Policies

In order to query the AWS Organizations, you either need to assume a role in the master payer account. Or you need to
delegate administration to another account. For more information read the [Delegated administrator for AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_delegate_policies.html) page.

Here you see the least privileged delegated administrator policy that you can use:  

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ListRoot",
      "Effect": "Allow",
      "Principal": { "AWS": "<Delegated Account>" },
      "Action": [ "organizations:ListRoots" ],
      "Resource": [ "*" ]
    },
    {
      "Sid": "ListContent",
      "Effect": "Allow",
      "Principal": { "AWS": "Delegated Account" },
      "Action": [
        "organizations:DescribeOrganizationalUnit",
        "organizations:DescribeAccount",
        "organizations:ListChildren"
      ],
      "Resource": [
        "arn:aws:organizations::<Master Payer Account>:account/*",
        "arn:aws:organizations::<Master Payer Account>:ou/*",
        "arn:aws:organizations::<Master Payer Account>:root/*"
      ]
    }
  ]
}
```

## Usage

You can use this module in the ways:

- [Using the CLI](./docs/using-cli.md)
- [Using AWS Lambda](./docs/using-lambda.md)
- [Using the python module](./docs/using-python-module.md)