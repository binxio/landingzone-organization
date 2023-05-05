---
title: "Using the CLI"
weight: 1
chapter: true
pre: "<b>1. </b>"
---

# Using the CLI

Before you can execute any command you need to select the correct profile:

```shell
export CUSTOMER=<prefix used in your profiles>
export AWS_PROFILE=${CUSTOMER}-audit
```

## Download the organization structure

Before you can use the CLI commands you need to execute the following command:

```shell
landingzone-organization organization download
```

This command will query the AWS Organization API and store the aggregated data to a file in the current working directory.
This file will be reused for every other command.

## Generate profiles for the AWS CLI

Managing profiles for the AWS CLI could become a nightmare when you have a lot of accounts.
To make it easier you can generate a separate config file for your organization.

```shell
AWS_CONFIG_FILE="~/.aws/config-acme" landingzone-organization profiles generate acme \
        --sso-start-url "https://acme.awsapps.com/start" \
        --sso-region "eu-central-1" \
        --role-session-name "John.Doe@acme.com" \
        --sso-role-name "my-sso-audit-role"
```

This will create a file called `~/.aws/config-acme` and when you set the `AWS_CONFIG_FILE` environment variable.

```shell
export AWS_CONFIG_FILE=~/.aws/config-acme
```

From now on the profiles are selected from your new "organization" config file. And you can use the account names within your organization as profiles:

```shell
aws s3 ls --profile <aws account name>
```

This will work as long as you have the right to assume the `my-sso-audit-role` role in the target account.

## List all workloads

To get an overview of all the workloads within your organization you can execute the following command:

```shell
landingzone-organization workload list [--location "<OU NAME>"]
```

When you want to list a nested OU you can use comma separation: 

```shell
landingzone-organization workload list [--location "<OU NAME>,<OU NAME>"]
```

## View account by ID

Sometimes you have an Account ID and you need to know what account it is. To get more information about the given
Account ID you can execute the following command:  

```shell
landingzone-organization account view <ACCOUNT_ID>
```