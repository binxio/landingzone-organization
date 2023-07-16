# CHANGELOG



## v0.6.0 (2023-07-16)

### Chore

* chore(deps-dev): bump mypy from 1.1.1 to 1.4.1 (#71)

Bumps [mypy](https://github.com/python/mypy) from 1.1.1 to 1.4.1.
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/3534bacc4c0d3c4b1983a533e2a36cce43f2ec9d&#34;&gt;&lt;code&gt;3534bac&lt;/code&gt;&lt;/a&gt;
Remove +dev from version&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/f36ea01e9de2ffac42a2615307f3692fd8e84c4a&#34;&gt;&lt;code&gt;f36ea01&lt;/code&gt;&lt;/a&gt;
Fix async iterator body stripping (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/15491&#34;&gt;#15491&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/ba7887be34391ae777cb32ca85719f3b3fa01c06&#34;&gt;&lt;code&gt;ba7887b&lt;/code&gt;&lt;/a&gt;
Revert &amp;quot;Fix spurious errors on builtins.open (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/15161&#34;&gt;#15161&lt;/a&gt;)&amp;quot;
(&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/15508&#34;&gt;#15508&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/16fe5da0bd9be4d0669f00a47d260894c988cf87&#34;&gt;&lt;code&gt;16fe5da&lt;/code&gt;&lt;/a&gt;
Fix readthedocs build (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/15437&#34;&gt;#15437&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/9b327d12bc3b57cc30ed76dcd3e07a3674da17a2&#34;&gt;&lt;code&gt;9b327d1&lt;/code&gt;&lt;/a&gt;
Use consistent anchors for error codes (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/15435&#34;&gt;#15435&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/32abe0210092e6e074d9c2cc1862a3cf7c2421c5&#34;&gt;&lt;code&gt;32abe02&lt;/code&gt;&lt;/a&gt;
docs: ref redirector (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/15432&#34;&gt;#15432&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/e5a5b33e12e850d8cf11e156267adf8ee85e6221&#34;&gt;&lt;code&gt;e5a5b33&lt;/code&gt;&lt;/a&gt;
Unbreak CI (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/15505&#34;&gt;#15505&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/81d01aa0bdec8f9c2ed85d39b6077572abcda72a&#34;&gt;&lt;code&gt;81d01aa&lt;/code&gt;&lt;/a&gt;
Fix PEP 561 editable install test case (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/15493&#34;&gt;#15493&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/eba351e4016a57fad611cc14cef456a741a4713b&#34;&gt;&lt;code&gt;eba351e&lt;/code&gt;&lt;/a&gt;
Add pip as test requirement for PEP 660 editable installs (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/15482&#34;&gt;#15482&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/9faffe87c0f15980afc041183148829208f4fc8f&#34;&gt;&lt;code&gt;9faffe8&lt;/code&gt;&lt;/a&gt;
Bump typing_extensions dependency (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/15488&#34;&gt;#15488&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/python/mypy/compare/v1.1.1...v1.4.1&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=mypy&amp;package-manager=pip&amp;previous-version=1.1.1&amp;new-version=1.4.1)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`ba5cdd2`](https://github.com/binxio/landingzone-organization/commit/ba5cdd21b23f7319fa898b19e9a72dda6242ddcf))

* chore(deps-dev): bump pytest-cov from 4.0.0 to 4.1.0 (#41)

Bumps [pytest-cov](https://github.com/pytest-dev/pytest-cov) from 4.0.0
to 4.1.0.
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/pytest-dev/pytest-cov/blob/master/CHANGELOG.rst&#34;&gt;pytest-cov&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;4.1.0 (2023-05-24)&lt;/h2&gt;
&lt;ul&gt;
&lt;li&gt;Updated CI with new Pythons and dependencies.&lt;/li&gt;
&lt;li&gt;Removed rsyncdir support. This makes pytest-cov compatible with
xdist 3.0.
Contributed by Sorin Sbarnea in
&lt;code&gt;[#558](https://github.com/pytest-dev/pytest-cov/issues/558)
&amp;lt;https://github.com/pytest-dev/pytest-cov/pull/558&amp;gt;&lt;/code&gt;_.&lt;/li&gt;
&lt;li&gt;Optimized summary generation to not be performed if no reporting is
active (for example,
when &lt;code&gt;--cov-report=&#39;&#39;&lt;/code&gt; is used without
&lt;code&gt;--cov-fail-under&lt;/code&gt;).
Contributed by Jonathan Stewmon in
&lt;code&gt;[#589](https://github.com/pytest-dev/pytest-cov/issues/589)
&amp;lt;https://github.com/pytest-dev/pytest-cov/pull/589&amp;gt;&lt;/code&gt;_.&lt;/li&gt;
&lt;li&gt;Added support for JSON reporting.
Contributed by Matthew Gamble in
&lt;code&gt;[#582](https://github.com/pytest-dev/pytest-cov/issues/582)
&amp;lt;https://github.com/pytest-dev/pytest-cov/pull/582&amp;gt;&lt;/code&gt;_.&lt;/li&gt;
&lt;li&gt;Refactored code to use f-strings.
Contributed by Mark Mayo in
&lt;code&gt;[#572](https://github.com/pytest-dev/pytest-cov/issues/572)
&amp;lt;https://github.com/pytest-dev/pytest-cov/pull/572&amp;gt;&lt;/code&gt;_.&lt;/li&gt;
&lt;li&gt;Fixed a skip in the test suite for some old xdist.
Contributed by a bunch of people in
&lt;code&gt;[#565](https://github.com/pytest-dev/pytest-cov/issues/565)
&amp;lt;https://github.com/pytest-dev/pytest-cov/pull/565&amp;gt;&lt;/code&gt;_.&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest-cov/commit/2c9f2170d8575b21bafb6402eb30ca7de31e20b9&#34;&gt;&lt;code&gt;2c9f217&lt;/code&gt;&lt;/a&gt;
Bump version: 4.0.0 → 4.1.0&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest-cov/commit/4d245df8f75e434a9e1b162b51265d6a45017465&#34;&gt;&lt;code&gt;4d245df&lt;/code&gt;&lt;/a&gt;
Update changelog and authors.&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest-cov/commit/7b095c84ae521b14058d7d520ef36372849063a8&#34;&gt;&lt;code&gt;7b095c8&lt;/code&gt;&lt;/a&gt;
Skip starting from xdist 3.0.2 (where boxed was removed).&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest-cov/commit/605d6902b3b3d17aad0bf811b8c580fc895724ca&#34;&gt;&lt;code&gt;605d690&lt;/code&gt;&lt;/a&gt;
disabling boxed test if version xdist newer than 2.5.0&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest-cov/commit/76fb2a6cb2c4a4a788a5b62710848daf9c8fb7ce&#34;&gt;&lt;code&gt;76fb2a6&lt;/code&gt;&lt;/a&gt;
introduced f-strings&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest-cov/commit/0d63ede0d2ca9f4acc8329aa4261a7cec489ffdb&#34;&gt;&lt;code&gt;0d63ede&lt;/code&gt;&lt;/a&gt;
Update test config. Reapply some of the changes from PR567 to the right
file ...&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest-cov/commit/f3d8d8380f6a4b265353fe7cd509b040702f1e64&#34;&gt;&lt;code&gt;f3d8d83&lt;/code&gt;&lt;/a&gt;
Add support for JSON reporter&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest-cov/commit/dec02abeb9fa8ee3547baa054bde6006bea530ee&#34;&gt;&lt;code&gt;dec02ab&lt;/code&gt;&lt;/a&gt;
Update test deps.&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest-cov/commit/88a7d348986bace58e26c88a713ef35f900ce2ef&#34;&gt;&lt;code&gt;88a7d34&lt;/code&gt;&lt;/a&gt;
chore: update AUTHORS and CHANGELOG&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest-cov/commit/74eb4cc8b684269b89735e31b623f0f9795c5d5c&#34;&gt;&lt;code&gt;74eb4cc&lt;/code&gt;&lt;/a&gt;
perf: only call summary when the report will be used&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/pytest-dev/pytest-cov/compare/v4.0.0...v4.1.0&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=pytest-cov&amp;package-manager=pip&amp;previous-version=4.0.0&amp;new-version=4.1.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

You can trigger a rebase of this PR by commenting `@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;
&gt; **Note**
&gt; Automatic rebases have been disabled on this pull request as it has
been open for over 30 days.

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`bf59393`](https://github.com/binxio/landingzone-organization/commit/bf593935fec075ad8ccc80de373b994b44f339c6))

* chore(deps-dev): bump pytest from 7.2.2 to 7.4.0 (#69) ([`e4731fa`](https://github.com/binxio/landingzone-organization/commit/e4731fa62cdb9bd50f9967e9976b04804f9f4afc))

* chore(deps-dev): bump aws-sam-cli from 1.78.0 to 1.90.0 (#81) ([`086a066`](https://github.com/binxio/landingzone-organization/commit/086a066ee32cfb756f0f660d9a60d3be871508a2))

* chore(deps): bump boto3 from 1.26.125 to 1.28.3 (#84)

Bumps [boto3](https://github.com/boto/boto3) from 1.26.125 to 1.28.3.
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/boto/boto3/blob/develop/CHANGELOG.rst&#34;&gt;boto3&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h1&gt;1.28.3&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;cognito-idp&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] API
model updated in Amazon Cognito&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;connect&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Add support
for deleting Queues and Routing Profiles.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;datasync&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Added
LunCount to the response object of
DescribeStorageSystemResourcesResponse, LunCount represents the number
of LUNs on a storage system resource.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;dms&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Enhanced
PostgreSQL target endpoint settings for providing Babelfish
support.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;ec2&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This release
adds support for the C7gn and Hpc7g instances. C7gn instances are
powered by AWS Graviton3 processors and the fifth-generation AWS Nitro
Cards. Hpc7g instances are powered by AWS Graviton 3E processors and
provide up to 200 Gbps network bandwidth.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;fsx&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Amazon FSx for
NetApp ONTAP now supports SnapLock, an ONTAP feature that enables you to
protect your files in a volume by transitioning them to a write once,
read many (WORM) state.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;iam&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Documentation
updates for AWS Identity and Access Management (IAM).&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;mediatailor&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Adds
categories to MediaTailor channel assembly alerts&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;personalize&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release provides ability to customers to change schema associated with
their datasets in Amazon Personalize&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;proton&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This release
adds support for deployment history for Proton provisioned
resources&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;s3&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] S3 Inventory now
supports Object Access Control List and Object Owner as available object
metadata fields in inventory reports.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;sagemaker&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Amazon
SageMaker Canvas adds WorkspeceSettings support for
CanvasAppSettings&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;secretsmanager&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Documentation updates for Secrets Manager&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.28.2&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;bugfix:s3: [&lt;code&gt;botocore&lt;/code&gt;] Fix s3 presigned URLs for
operations with query components
(&lt;code&gt;[#2962](https://github.com/boto/boto3/issues/2962)
&amp;lt;https://github.com/boto/botocore/issues/2962&amp;gt;&lt;/code&gt;__)&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;cognito-idp&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] API
model updated in Amazon Cognito&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.28.1&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;dms&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Releasing DMS
Serverless. Adding support for PostgreSQL 15.x as source and target
endpoint. Adding support for DocDB Elastic Clusters with sharded
collections, PostgreSQL datatype mapping customization and disabling
hostname validation of the certificate authority in Kafka endpoint
settings&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;glue&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This release
enables customers to create new Apache Iceberg tables and associated
metadata in Amazon S3 by using native AWS Glue CreateTable
operation.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;logs&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Add CMK
encryption support for CloudWatch Logs Insights query result data&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;medialive&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release enables the use of Thumbnails in AWS Elemental MediaLive.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;mediatailor&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] The AWS
Elemental MediaTailor SDK for Channel Assembly has added support for
EXT-X-CUE-OUT and EXT-X-CUE-IN tags to specify ad breaks in HLS outputs,
including support for EXT-OATCLS, EXT-X-ASSET, and EXT-X-CUE-OUT-CONT
accessory tags.&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.28.0&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;enhancement:configprovider: [&lt;code&gt;botocore&lt;/code&gt;] Always use
shallow copy of session config value store for clients&lt;/li&gt;
&lt;li&gt;feature:configuration: [&lt;code&gt;botocore&lt;/code&gt;] Configure the
endpoint URL in the shared configuration file or via an environment
variable for a specific AWS service or all AWS services.&lt;/li&gt;
&lt;li&gt;bugfix:configprovider: [&lt;code&gt;botocore&lt;/code&gt;] Fix bug when deep
copying config value store where overrides were not preserved&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;ec2&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Add Nitro
Enclaves support on DescribeInstanceTypes&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;location&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release adds support for authenticating with Amazon Location Service&#39;s
Places &amp;amp; Routes APIs with an API Key. Also, with this release
developers can publish tracked device position updates to Amazon
EventBridge.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;outposts&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Added
paginator support to several APIs. Added the ISOLATED enum value to
AssetState.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;quicksight&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release includes below three changes: small multiples axes improvement,
field based coloring, removed required trait from Aggregation function
for TopBottomFilter.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;rds&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Updates Amazon
RDS documentation for creating DB instances and creating Aurora global
clusters.&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.27.1&lt;/h1&gt;
&lt;!-- raw HTML omitted --&gt;
&lt;/blockquote&gt;
&lt;p&gt;... (truncated)&lt;/p&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/618d2b9281913b6acbf9e3e432fc6f5c48c8229c&#34;&gt;&lt;code&gt;618d2b9&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.28.3&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/1d41697a41466733a1e271a59d9cb7a07f92d206&#34;&gt;&lt;code&gt;1d41697&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.28.3&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/643a04bebf5a55fd10978371cbd5bfec16937e15&#34;&gt;&lt;code&gt;643a04b&lt;/code&gt;&lt;/a&gt;
Add changelog entries from botocore&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/132613ebbd96efef1277743318791186f2b1a8f0&#34;&gt;&lt;code&gt;132613e&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.28.2&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/6671104a0ccc145a20d6d29f128d1422091bcb02&#34;&gt;&lt;code&gt;6671104&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.28.2&#39; into develop&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/b107765ccab7f43ba651ec321adcdd9a32a5eb75&#34;&gt;&lt;code&gt;b107765&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.28.2&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/fe0be41d24d9f98bd526e47d41fb4a4fa2ac6b5b&#34;&gt;&lt;code&gt;fe0be41&lt;/code&gt;&lt;/a&gt;
Add changelog entries from botocore&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/53a0c84b2e016f0491a8ebf34b3d902e71207c37&#34;&gt;&lt;code&gt;53a0c84&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.28.1&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/3c988a24f22795d3cb9cf26a74c085d2e6a58504&#34;&gt;&lt;code&gt;3c988a2&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.28.1&#39; into develop&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/eaa5d94bfc7e6720ebd73dbfa01bfc9b7be8da6d&#34;&gt;&lt;code&gt;eaa5d94&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.28.1&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/boto/boto3/compare/1.26.125...1.28.3&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=boto3&amp;package-manager=pip&amp;previous-version=1.26.125&amp;new-version=1.28.3)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`588738c`](https://github.com/binxio/landingzone-organization/commit/588738ccc39cc7ee2fece8d5d79d3bccab11e151))

### Feature

* feat: return environments in DTAP order (#85)

**Issue #, if available:**

## Description of changes:

When you retrieve the environments you used to get a random order. With
this feature you will have the ability to customize the order. By
default we follow the DTAP order as in Development, Testing, Acceptance
and Production.

**Checklist**

&lt;!--- Leave unchecked if your change doesn&#39;t seem to apply --&gt;

* [x] Update tests
* [x] Update docs
* [x] PR title follows [conventional commit
semantics](https://www.conventionalcommits.org/en/v1.0.0-beta.2/#commit-message-for-a-fix-using-an-optional-issue-number)

By submitting this pull request, I confirm that you can use, modify,
copy, and redistribute this contribution, under the terms of your
choice. ([`86d2a89`](https://github.com/binxio/landingzone-organization/commit/86d2a89436035c1e8ba68720c30e381ae07f3d46))


## v0.5.0 (2023-06-20)

### Documentation

* docs: add sso context and improve installation instructions (#26)

**Issue #, if available:**

## Description of changes:

&lt;!--- One or two sentences as a summary of what&#39;s being changed --&gt;

**Checklist**

&lt;!--- Leave unchecked if your change doesn&#39;t seem to apply --&gt;

* [x] Update tests
* [x] Update docs
* [x] PR title follows [conventional commit
semantics](https://www.conventionalcommits.org/en/v1.0.0-beta.2/#commit-message-for-a-fix-using-an-optional-issue-number)

By submitting this pull request, I confirm that you can use, modify,
copy, and redistribute this contribution, under the terms of your
choice. ([`2ee6ed3`](https://github.com/binxio/landingzone-organization/commit/2ee6ed3cf7c1c08fa521e8d4ee6d831356960d31))

### Feature

* feat: create an export of all accounts (#62)

**Issue #, if available:**

## Description of changes:

Add the ability to create an export of all AWS Accounts available in the
organization. This will help with reporting for example.

**Checklist**

&lt;!--- Leave unchecked if your change doesn&#39;t seem to apply --&gt;

* [x] Update tests
* [x] Update docs
* [x] PR title follows [conventional commit
semantics](https://www.conventionalcommits.org/en/v1.0.0-beta.2/#commit-message-for-a-fix-using-an-optional-issue-number)

By submitting this pull request, I confirm that you can use, modify,
copy, and redistribute this contribution, under the terms of your
choice. ([`87ae09e`](https://github.com/binxio/landingzone-organization/commit/87ae09e58b611948441443b30a5c5ad61857a430))


## v0.4.0 (2023-05-05)

### Feature

* feat: add profiles class to fetch available profiles for automation (#24)

**Issue #, if available:**

## Description of changes:

When we have generated a profiles file you probably want to use it to
automate things. By offering a profiles class to read the generated file
we make it easier to write use-cases that you can then run against all
generated profiles.

**Checklist**

&lt;!--- Leave unchecked if your change doesn&#39;t seem to apply --&gt;

* [x] Update tests
* [x] Update docs
* [x] PR title follows [conventional commit
semantics](https://www.conventionalcommits.org/en/v1.0.0-beta.2/#commit-message-for-a-fix-using-an-optional-issue-number)

By submitting this pull request, I confirm that you can use, modify,
copy, and redistribute this contribution, under the terms of your
choice. ([`7da773b`](https://github.com/binxio/landingzone-organization/commit/7da773bf22eb6ab616d305dbf24b9fee15af806f))


## v0.3.0 (2023-05-04)

### Documentation

* docs: improve module example and add pytest example ([`161db05`](https://github.com/binxio/landingzone-organization/commit/161db05cac4352a92f3eacbead8bdc527bf5a743))

* docs: fixed typo ([`ae52130`](https://github.com/binxio/landingzone-organization/commit/ae52130da3caa69ff18761e39f7f93e8c289ea3f))

* docs: fix image reference ([`589e021`](https://github.com/binxio/landingzone-organization/commit/589e021265a3ab8a25b71273baa0b0e840771094))

* docs: improve the aws lambda documentation ([`570d726`](https://github.com/binxio/landingzone-organization/commit/570d7266a99803a8e4be5eba1a0befc801d92806))

* docs: fix code references and policy content

The policy included text without brackets, this could suggest that you do not need to replace it with an account id. Also the code references were broken after the instructions where moved from the main readme to the documentation pages. ([`6b30d6b`](https://github.com/binxio/landingzone-organization/commit/6b30d6b86875d7f87e408500ecfb8ad038b09194))

### Feature

* feat: generate profiles for aws cli tool (#22)

**Issue #, if available:**

## Description of changes:

Managing profiles for the AWS cli could become a nightmare when you have
a lot of accounts. To make it easier you can generate a separate config
file for your organization.

**Checklist**

&lt;!--- Leave unchecked if your change doesn&#39;t seem to apply --&gt;

* [x] Update tests
* [x] Update docs
* [x] PR title follows [conventional commit
semantics](https://www.conventionalcommits.org/en/v1.0.0-beta.2/#commit-message-for-a-fix-using-an-optional-issue-number)

By submitting this pull request, I confirm that you can use, modify,
copy, and redistribute this contribution, under the terms of your
choice. ([`f218ad2`](https://github.com/binxio/landingzone-organization/commit/f218ad22a1cd1377509d3e3b973a53a4f033330e))

### Test

* test: use unique ou ids and remove unneeded code ([`254e4b2`](https://github.com/binxio/landingzone-organization/commit/254e4b29e67005917ad98b2eecd8e518ceccdcd1))


## v0.2.2 (2023-05-03)

### Fix

* fix: correctly link to user documentation (#20)

**Issue #, if available:**

## Description of changes:

Link to the homepage still did not resolve correctly with the previous
fix. Renamed the `Usage` section to `User Documentation` and added a
direct link to the `User Documentation`.

**Checklist**

&lt;!--- Leave unchecked if your change doesn&#39;t seem to apply --&gt;

* [x] Update tests
* [x] Update docs
* [x] PR title follows [conventional commit
semantics](https://www.conventionalcommits.org/en/v1.0.0-beta.2/#commit-message-for-a-fix-using-an-optional-issue-number)

By submitting this pull request, I confirm that you can use, modify,
copy, and redistribute this contribution, under the terms of your
choice. ([`eb72dc5`](https://github.com/binxio/landingzone-organization/commit/eb72dc51435ef435aec79937ec6d3f71431f2510))


## v0.2.1 (2023-05-03)

### Chore

* chore(deps): bump boto3 from 1.26.124 to 1.26.125 (#17)

Bumps [boto3](https://github.com/boto/boto3) from 1.26.124 to 1.26.125.
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/boto/boto3/blob/develop/CHANGELOG.rst&#34;&gt;boto3&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h1&gt;1.26.125&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;appflow&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release adds new API to cancel flow executions.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;connect&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Amazon
Connect Service Rules API update: Added OnContactEvaluationSubmit event
source to support user configuring evaluation form rules.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;ecs&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Documentation
only update to address Amazon ECS tickets.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;kendra&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] AWS Kendra
now supports configuring document fields/attributes via the
GetQuerySuggestions API. You can now base query suggestions on the
contents of document fields.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;resiliencehub&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release will improve resource level transparency in applications by
discovering previously hidden resources.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;sagemaker&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Amazon
Sagemaker Autopilot supports training models with sample weights and
additional objective metrics.&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/0458ce94a4a3371b83775dbc6cc2e75a30f686bd&#34;&gt;&lt;code&gt;0458ce9&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.26.125&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/3b55431d85be4b4c455c1b81932a8f2d59ae26a9&#34;&gt;&lt;code&gt;3b55431&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.26.125&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/7a9afbf64eef5e08473c3abc858380700e07ebc2&#34;&gt;&lt;code&gt;7a9afbf&lt;/code&gt;&lt;/a&gt;
Add changelog entries from botocore&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/84e71bd1902b1c71784654ca5e8c01dab82c62ed&#34;&gt;&lt;code&gt;84e71bd&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.26.124&#39; into develop&lt;/li&gt;
&lt;li&gt;See full diff in &lt;a
href=&#34;https://github.com/boto/boto3/compare/1.26.124...1.26.125&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=boto3&amp;package-manager=pip&amp;previous-version=1.26.124&amp;new-version=1.26.125)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt;
Co-authored-by: Joris Conijn &lt;joris.conijn@xebia.com&gt; ([`10e6a45`](https://github.com/binxio/landingzone-organization/commit/10e6a4517d471833977d9ab0312b43485715ca59))

### Documentation

* docs: introduce documentation hosted on GitHub pages (#18)

**Issue #, if available:**

## Description of changes:

To make it easier to use the module user documentation is needed. By
offering this through GitHub pages we have a nice interactive website
that helps you with that.

**Checklist**

&lt;!--- Leave unchecked if your change doesn&#39;t seem to apply --&gt;

* [x] Update tests
* [x] Update docs
* [x] PR title follows [conventional commit
semantics](https://www.conventionalcommits.org/en/v1.0.0-beta.2/#commit-message-for-a-fix-using-an-optional-issue-number)

By submitting this pull request, I confirm that you can use, modify,
copy, and redistribute this contribution, under the terms of your
choice. ([`78f7343`](https://github.com/binxio/landingzone-organization/commit/78f7343c679739fc9e7d806e5b9459365213da90))

* docs: tweak the readme a bit to trigger a new release ([`aa52f94`](https://github.com/binxio/landingzone-organization/commit/aa52f94a4fdc3c02919f6caed66f497206f074c2))

### Fix

* fix: homepage url in package and links within documentation (#19)

**Issue #, if available:**

## Description of changes:

The package on pipit did not include the proper links to the bug
trackers and user documentation. Also some of the Hugo redirects where
not functioning as they should so fixed that by applying a workaround.

**Checklist**

&lt;!--- Leave unchecked if your change doesn&#39;t seem to apply --&gt;

* [x] Update tests
* [x] Update docs
* [x] PR title follows [conventional commit
semantics](https://www.conventionalcommits.org/en/v1.0.0-beta.2/#commit-message-for-a-fix-using-an-optional-issue-number)

By submitting this pull request, I confirm that you can use, modify,
copy, and redistribute this contribution, under the terms of your
choice. ([`eb232f4`](https://github.com/binxio/landingzone-organization/commit/eb232f42a696c1377c1a54e46bc436fc13f097f3))

### Unknown

* Merge pull request #15 from binxio/develop

docs: tweak the readme a bit to trigger a new release ([`0184480`](https://github.com/binxio/landingzone-organization/commit/0184480dcb2a04187bcd407af982b538e5c689ea))


## v0.2.0 (2023-05-02)

### Chore

* chore: tweak the ci process ([`964e69e`](https://github.com/binxio/landingzone-organization/commit/964e69e2730918d851f4eb7b186059a87a97e2e1))

* chore: previous version was v0.1.0 ([`9080cdf`](https://github.com/binxio/landingzone-organization/commit/9080cdfdbfffdf30824d72242a9db4af8565dc67))

* chore: previous version was 0.1.0 ([`72d1a17`](https://github.com/binxio/landingzone-organization/commit/72d1a17f048d0d484ff562251f63339c5020b584))

* chore: trigger a new version to be released ([`e268ba5`](https://github.com/binxio/landingzone-organization/commit/e268ba549d118eaf57d79535b6bc3f99df90ad2f))

* chore: disable other jobs ([`5797a7b`](https://github.com/binxio/landingzone-organization/commit/5797a7b5ed314284775964386a711878be316d9d))

* chore(deps): bump boto3 from 1.26.98 to 1.26.124 (#7)

Bumps [boto3](https://github.com/boto/boto3) from 1.26.98 to 1.26.124.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.26.98...1.26.124)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;

---------

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: Joris Conijn &lt;joris.conijn@xebia.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`2f354be`](https://github.com/binxio/landingzone-organization/commit/2f354beca5335e960fc018db51f98653dbd66b48))

* chore: tweak ci process ([`107cea0`](https://github.com/binxio/landingzone-organization/commit/107cea0169b27857453c118eb4a72262ccadff6d))

* chore: tweak the release process (#8)

* chore: tweak the release process
* chore: add the develop branch as a quality trugger ([`95ccc3a`](https://github.com/binxio/landingzone-organization/commit/95ccc3a6d39bd5d0d2210359f5b8c0ba1987881f))

* chore: add the develop branch as a quality trugger ([`4ec6ff2`](https://github.com/binxio/landingzone-organization/commit/4ec6ff2c7a5ee214f293103b6463b6b2c5935e08))

* chore: tweak the release process

Attempt to automatically bump the version on releases ([`d496388`](https://github.com/binxio/landingzone-organization/commit/d496388ab8f3f5fa6ad0a804315482fd7a30c779))

* chore: disable coverage (#6)

We did not configure coverage for binx owned repositories. ([`5633991`](https://github.com/binxio/landingzone-organization/commit/5633991f6dab0ecc845bca13a1bcfdd160f2e01f))

### Feature

* feat: initial commit ([`26fa7e3`](https://github.com/binxio/landingzone-organization/commit/26fa7e3accaf162e7cdd757ad7b86d131ef478f0))

### Fix

* fix: correct typo ([`27b6609`](https://github.com/binxio/landingzone-organization/commit/27b6609f7293d86b370c33ed2fd8bfe010de0326))

* fix: use correct version path ([`34526cc`](https://github.com/binxio/landingzone-organization/commit/34526cca74437c46575befeaa91dc32498e630a3))

### Unknown

* Merge pull request #14 from binxio/develop

fix: correct typo ([`c70c748`](https://github.com/binxio/landingzone-organization/commit/c70c748a43cc276d33c3947189868039fa5bab56))

* Merge pull request #13 from binxio/develop

fix: use correct version path ([`974897e`](https://github.com/binxio/landingzone-organization/commit/974897e8ea8f090f9fdccb9a1377cfbc8d094c54))

* 0.1.0 ([`f87d472`](https://github.com/binxio/landingzone-organization/commit/f87d47258cb9cf55850320d2c71d2279afe03db4))

* Merge pull request #11 from binxio/develop

chore: previous version was 0.1.0 ([`49ee418`](https://github.com/binxio/landingzone-organization/commit/49ee4182d21cb90254aff8e8b376d7fc47de989f))

* Merge branch &#39;main&#39; into develop ([`886327a`](https://github.com/binxio/landingzone-organization/commit/886327a778a056b08c1b2a8ac4dc8083ce73fc09))

* Merge pull request #10 from binxio/develop

chore: trigger a new version to be released ([`5e8cabb`](https://github.com/binxio/landingzone-organization/commit/5e8cabb881ded2ae7f4eff64a5e2d33eff547075))

* Merge pull request #9 from binxio/develop

chore: test release cycle ([`dbcb4eb`](https://github.com/binxio/landingzone-organization/commit/dbcb4ebdd8561f4443c2269c9ae8378ced55d8c9))

* Merge branch &#39;main&#39; into develop ([`bbf9539`](https://github.com/binxio/landingzone-organization/commit/bbf95390e356ab1ff4554e4de651b9ff3863e37c))
