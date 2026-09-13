# Submission-Ready Checklist

**Candidate:** Manoher Singh  
**Role:** Junior Cloud & DevOps Engineer (Google Cloud Platform / Django / React)  
**Deadline:** 13 September 2026

## Recommended upload

Upload the ZIP containing this folder as the project submission. The ZIP includes the source, tests, spreadsheet, documentation, and 14-slide presentation.

## Before the one-time submission

- [x] Candidate name/contact details reviewed.
- [x] Terraform source included with runtime project/bucket inputs.
- [x] GCS raw landing security controls included.
- [x] BigQuery staged/enforced table and row-level policy included.
- [x] Fail-closed GitHub Actions workflow included.
- [x] Gitleaks and deterministic secret scan included.
- [x] Django REST Framework serializer included.
- [x] Binary DCYN decision library included.
- [x] Valid and invalid onboarding examples included.
- [x] Schema workbook included.
- [x] 14-slide presentation included (within the 15-slide limit).
- [x] Assumptions are explicitly documented.
- [x] No real credentials or secrets are included.

## Validation status in this environment

- Python compilation: **PASS**
- DCYN/contract tests: **8 PASS**
- Deterministic secret scan: **PASS**
- Fail-closed demo: **PASS** — intentionally blocks the generated fake secret
- Django/DRF serializer tests: **not executed here** because Django/DRF packages are not installed and this environment has no package-network access. The CI workflow installs the declared dependencies and runs the serializer tests.
- Terraform CLI validation: **not executed here** because Terraform CLI is not installed. The CI workflow performs formatting, initialization, validation, TFLint and Checkov gates.

Do not describe the unexecuted Terraform or DRF checks as locally passed. The repository is designed so those checks run in CI or in a local environment with the declared dependencies/tools installed.
