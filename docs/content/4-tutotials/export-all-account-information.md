---
title: "Export all account information"
weight: 2
chapter: true
pre: "<b>2. </b>"
---

# Export all account information

Creating an export of all AWS accounts in your AWS organization can be useful for several reasons. 
Firstly, it can help you keep track of all the accounts that are part of your organization, which can be helpful if you need to manage or audit them. 
Secondly, having an export of all accounts can help you identify any unused or unnecessary accounts that can be deleted to save costs. 
Additionally, it can help you monitor the usage of resources across all accounts, which can help you optimize your AWS infrastructure. 
Finally, having an export of all accounts can be helpful for compliance and regulatory purposes, as it provides a comprehensive record of all accounts in your organization.

The following command will generate a CSV file based on the current organization information:

```shell
landingzone-organization account export my-file-name.csv
```
