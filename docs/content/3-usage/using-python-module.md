---
title: "Sample using as a python module"
weight: 3
chapter: true
pre: "<b>3. </b>"
---

# Sample using as a python module 

List all workload accounts name and id

```python
import boto3

# Assume role in audit account
organization = Organization() # Fetch organizational data

# Use normale SSO profile

for workload in organization.all_accounts:
    for account in workload.accounts:
        # Assume a role in the target account
        session = sts_client.assume_role(f"arn::{account.id}:role/my-role-name")
        
        # Fetch information
        ec2_client = boto3.client(session)
        ec2_client.describe_instances()
        
#         Use the sts_caller_identity as an example

```
