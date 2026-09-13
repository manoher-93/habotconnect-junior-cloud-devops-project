# Interview Quick Guide

## 1. Explain the architecture in 30 seconds

"I separated the solution into three controls. GCS is the D0 raw landing layer, BigQuery is the D1 staged/enforced layer, and GitHub Actions is the Poka-Yoke control that prevents unsafe changes from reaching deployment. IAM controls which identities can act, while BigQuery row-level security controls which rows a permitted analytics identity can see."

## 2. Why fail closed?

"A security or quality check should not be advisory if the requirement is to prevent an unsafe deployment. Every gate returns non-zero on failure, and deployment explicitly depends on the build-gate job succeeding."

## 3. Why both Gitleaks and a deterministic scanner?

"Gitleaks is the primary secret-detection control. The small deterministic scanner makes the assignment's hardcoded-secret rule easy to demonstrate and test locally. It is a defense-in-depth control, not a replacement for Gitleaks."

## 4. Explain row-level security

"Table IAM answers whether the identity can access the table. The row access policy then restricts the rows visible to the analytics identity based on organization_id. BigQuery automatically grants its filtered-data viewer permission through the row access policy."

## 5. Explain DCYN

"The business decision is intentionally binary: Yes or No. I added stable reason codes such as D003 for an invalid Universally Unique Identifier so a rejected record can be diagnosed consistently without introducing a human 'maybe' branch."

## 6. Why no production deployment claim?

"No Google Cloud credentials or dedicated project were supplied with the assessment, so I kept project_id and bucket name as runtime inputs and documented the Terraform validation and deployment commands rather than pretending a deployment occurred."

## 7. Be transparent about assumptions

"The brief requests exact validation limits but does not include the source JSON or a separate limit table. I made the contract explicit and executable so an evaluator can see exactly what I assumed and change it if the source contract differs."
