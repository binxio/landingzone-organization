# CloudFormation Example

Here you will find a sample how you could use this package within an AWS Lambda function. For now, it is a simple example.

Things that you could do for example is:

- Run this Lambda each x hours and store it on S3. This way you don't need to query the AWS Organizations API everytime.
- Use StepFunctions to get the organization data and do follow-up processing using the organization information.

