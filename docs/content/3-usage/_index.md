---
title: "Usage"
weight: 2
chapter: true
pre: "<b>3. </b>"
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