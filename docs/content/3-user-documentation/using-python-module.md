---
title: "Using the python module"
weight: 3
chapter: true
pre: "<b>3. </b>"
---

# Using the python module 

> For this to work, I assume you have configured your AWS cli correctly. You will need the configured profile name in order to test your script. If the default profile is used you can omit the environment variable. 

## Preparation

First you will need to have a place where to run the code. For simplicity’s sake this example will use the `venv` module to create an environment. You can create a virtual environment and activate it as followed: 

```shell
python -m venv .venv
source .venv/bin/activate
```

Next you will need to install the module as e dependency:

```shell
pip install landingzone-organization
```

## Build your script

Now we can start using it in your python scripts, for example create a `list_workload_environments.py` file with the following content:

```python
from landingzone_organization import AWSOrganization

# Fetch the organization information and instantiate the organization object 
organization = AWSOrganization().parse()

# Define the OU structure where the workload accounts live
nested_ou = ["Workloads"]

# Iterate over all workloads in the provided OU location 
for workload in organization.workloads(nested_ou):
    # Display the workload name
    print(f"Workload: {workload.name}")

    # Iterate over each account in the workload
    for account in workload.accounts:
        # Display the environment name and id of the account (aka the workload environment)
        print(f"\tEnvironment: {account.environment} has {account.account_id}")
```

## Test your script

Now you can simply run:

```shell
AWS_PROFILE=<YOUR CONFIGURED PROFILE> python list_workload_environments.py
```
