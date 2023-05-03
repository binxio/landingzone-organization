---
title: "Introduction"
weight: 1
chapter: true
pre: "<b>1. </b>"
---

# Introduction

The idea of this module was created from a specific need. And that need was to gain insight in what workloads are running within your organization.
Off course, you can keep track of all these things in Excel sheets. But at the time of writing they are already outdated! And it cost a lot of manual labor! 

So this module was build with the idea to use the actual state in the Cloud provider as a base. This means it will query the accounts/projects and based on logic it will categorize it.
This allows you to for example fetch all names of the workloads that have at least 1 environment. Or list all environment available to a workload.

The idea is to use this as a foundation to do other things with this information!

## Compatability

We aim to be cloud-agnostic, but today we are only compatible with one cloud provider. 

### AWS Organizations

This module has support for [AWS Organizations](https://aws.amazon.com/organizations/). 
