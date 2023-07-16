---
title: "Configuration"
weight: 2
chapter: true
pre: "<b>2. </b>"
---

# Configuration

By default, this package does an assumption about your naming schema. It expects you use the following format:
`<PREFIX>-<WORKLOAD NAME>-<ENVIRONMENT>`. When you deviate from this schema you potentially need to provide 2 configuration
options. You can do this via 2 environment variable:

| **Name**                 | **Default Value** | **Description**                                                                                               |
|--------------------------|-------------------|---------------------------------------------------------------------------------------------------------------|
| PATTERN_WORKLOAD_NAME    | `.*?-(.*)-.*`     | The first match is used as the workload name.                                                                 |
| PATTERN_ENVIRONMENT_NAME | `.*-.*-(.*)`      | The first match is used as the environment name. For example: development, testing, acceptance or production. |

## Other environment variable

| **Name**           | **Default Value** | **Description**                                                                                                                        |
|--------------------|-------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| ENVIRONMENT_WEIGHT | dev,test,acc,prod | The order that the environments are returned, we match using a startswith. If the environment does not match it will be returned last. |

## AWS Policies

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
      "Principal": { "AWS": "<Delegated Account>" },
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