---
title: "Execute a use-case against all profiles"
weight: 1
chapter: true
pre: "<b>1. </b>"
---

# Execute a use-case against all profiles

Sometimes you just want to know what the specific status is across all AWS accounts. For example, you might want to know if there are any AWS Accounts that have alarms in an **ALARM** state.
You could log in to each and every account, lookup the status and switch to all regions you are interested in. Or, you would write a script to assume a role in each account and use that to query the data.

Event in the last example the effort to assume the role and select the right region is something you need to duplicate for each use-case. So for me, it made sense to provide some light weight logic to help you with this.

## Requirements

Required tooling:

* [AWS CLI](https://aws.amazon.com/cli/)
* [Poetry](https://python-poetry.org)

## Preparation

You will need to have access to a role via SSO in all AWS Accounts. This role can be least privileged for what you want to do a typical audit role will work for most of the questions you most likely have.

Setup SSO:

```shell
$ aws configure sso
SSO session name (Recommended): my-sso
SSO start URL [None]: https://my-sso-portal.awsapps.com/start
SSO region [None]: us-east-1
SSO registration scopes [None]: sso:account:access
```

The process will start a web browser, this will ask you to **Allow** the AWS CLI to login. Afterwards the CLI will ask you what role you would like to assume.
Here you will need to select a role in the delegated administrator account for AWS Organizations. (Typically your Audit account)

Clone the repository and install all dependencies:

```shell
git clone git@github.com:binxio/landingzone-organization.git
cd landingzone-organization
poetry install
```

Next, so first you need to download the organization structure:

```shell
export AWS_PROFILE=my-sso
poetry run landingzone-organization organization download
```

Then you need to generate a **separate** config file for your profiles. We are using a separate file because we will read it later, and we do not want to overwrite your existing profiles.

```shell
export AWS_CONFIG_FILE="~/.aws/config-acme"
poetry run landingzone-organization profiles generate acme \
        --sso-start-url "https://my-sso-portal.awsapps.com/start" \
        --sso-region "us-east-1" \
        --role-session-name "John.Doe@acme.com" \
        --sso-role-name "my-sso-audit-role"
```

Next you will need to make sure you have an active SSO session by logging into one of the profiles.

```shell
aws sso login --profile <audit account name>
```

## Run the sample code

Now you should be able to run the example as followed:

```shell
poetry run ./examples/list_alarms.py
```

## Let's explore the use-case

There are 2 main files used here:

- [`examples/cloudwatch.py`](https://github.com/binxio/landingzone-organization/blob/main/examples/cloudwatch.py), contains a dataclass and the logic to fetch the data using the AWS APIs.
- [`examples/list_alarms.py`](https://github.com/binxio/landingzone-organization/blob/main/examples/list_alarms.py), orchestrates the execution and visualizes the results in a user-friendly manner.

So the **examples/list_alarms.py** file does some default checks, and once those passed it will do:

```python
executor = Profiles(config_file)
executor.execute(regions, adapter.get_alarms)
```

The **Profiles** class is provided by the **landingzone-organization** module and accepts a filepath. This is the file that we have written when we generated the profiled earlier.
Next we are providing it with a list of regions that we want to use and a **callback** method.

In essence what this does for you, it will:

1. Fetch all profiles in the given config file.
2. For each profile it will create a botocore session.
3. It will use the callback method to perform a callback with a session and a region. (this will be repeated for each region and profile)
4. Done.

Client errors are handled for you, and you are able to retrieve them from the **executor**:

```python
for client_exception in executor.client_exceptions:
    print(
        f"\t{client_exception} failed due to: {executor.client_exceptions[client_exception]}"
    )
```

The **examples/cloudwatch.py** file only contains the logic to be executed in the given region using the given session. How you structure this is entirely up to you ofcourse this is just an example how you could do it.

## Closing thoughts

By focussing on what data you want to extract from a single account and region.
You simplify your implementation and when you combine this with the **landingzone-organization** module.
You immediately can scale it to be executed in any region and account in your organization.
As long as you have the access to assume the role.
