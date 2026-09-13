# HabotConnect Hiring Project — Junior Cloud & DevOps Engineer

**Candidate:** Manoher Singh  
**Position:** Junior Cloud & DevOps Engineer (GCP / Django / React)  
**Contact:** manoharmsp93@gmail.com | +91-9648548275  
**Submission date:** 13 September 2026

## 1. Objective

This submission addresses the three tasks in the HabotConnect hiring project:

1. Secure Terraform provisioning for a GCS raw landing bucket and a BigQuery staged/enforced dataset, including least-privilege IAM, IAM conditions, and row-level security.
2. A fail-closed GitHub Actions build gate that blocks non-compliant infrastructure/application changes, including formatting failures and hardcoded secrets.
3. A deterministic Django REST Framework serializer and DCYN (Do/Can/Yes/No) decision library for a student onboarding payload.

The implementation is intentionally modular and reviewable. No production credentials are stored in the repository.

## 2. Repository layout

```text
terraform/
  versions.tf
  variables.tf
  main.tf
  iam.tf
  bigquery.tf
  app_engine.tf

src/
  serializers.py
  dcyn.py

tests/
  test_dcyn.py
  test_serializer.py

scripts/
  check_secrets.py

data/
  student_onboarding_schema.csv

.github/workflows/
  fail-closed.yml

docs/
  architecture.md
  validation-matrix.md

presentation/
  HabotConnect_Hiring_Project_Manoher_Singh.pptx
```

## 3. Security design

### GCS D0 Raw Landing

- Uniform bucket-level access is enabled.
- Public access prevention is enforced.
- Versioning is enabled to reduce accidental data-loss risk.
- A retention policy prevents premature deletion.
- IAM is granted to a dedicated service account rather than broad project members.
- Object access is constrained with a resource-name IAM condition.
- No credential is embedded in Terraform.

### BigQuery D1 Staged/Enforced

- Dataset access is managed explicitly.
- A dedicated staging service account receives only the roles required for data ingestion/querying.
- A sample student onboarding table is created so the requested BigQuery row-level security can be demonstrated as executable Terraform.
- The row access policy limits rows using a tenant/organization attribute.
- Dataset/table IAM is intentionally separated from row-level filtering: IAM determines who may access the data, while the row access policy determines which rows are visible.

### CI/CD Poka-Yoke

The workflow is fail-closed:

1. Terraform formatting check.
2. Terraform validation.
3. TFLint.
4. Checkov IaC security scan.
5. Gitleaks secret scan.
6. Deterministic repository secret-pattern scan.
7. Python compilation and unit tests.

A deployment job is deliberately placed after the build-gate job. If any gate fails, the workflow stops before deployment. This implements the project's "do not rely on human memory" requirement.

## 4. DCYN assumption

The hiring document requires a student-onboarding JSON payload but does not provide a concrete payload or exact field limits. Therefore this submission defines an explicit, deterministic contract rather than silently inventing an unseen source payload.

The assumed onboarding contract is documented in `docs/validation-matrix.md` and `data/student_onboarding_schema.csv`. Every assumption is represented as an executable serializer validation rule and a DCYN decision rule.

This is preferable to accepting arbitrary fields or relying on human judgement.

## 5. Running locally

### Python

```bash
python -m venv .venv
source .venv/bin/activate
pip install "Django>=5.2,<6" "djangorestframework>=3.16,<3.17"
python -m unittest discover -s tests -v
python -m compileall src tests
```

### Terraform

```bash
cd terraform
terraform fmt -check -recursive
terraform init
terraform validate
```

A real GCP project and authenticated Google Cloud credentials are required for `terraform plan` / `terraform apply`.

Example:

```bash
terraform plan \
  -var="project_id=YOUR_GCP_PROJECT_ID" \
  -var="environment=staging"
```

The project ID is an input, not a hardcoded credential or secret. The configuration targets the current Google Terraform provider 8.2.x series used by this submission.

## 6. Design decisions

### Why GCS + BigQuery instead of a single data store?

The scenario describes a D0 raw landing layer and D1 staged/enforced layer. GCS is appropriate for immutable/raw object landing, while BigQuery provides structured analytics and policy-controlled access.

### Why both IAM conditions and row-level security?

They solve different problems:

- IAM / IAM Conditions: *who* can perform an operation and under what resource/context constraints.
- BigQuery RLS: *which rows* an authorized principal can see.

Using both provides defense in depth.

### Why Gitleaks plus a deterministic secret scanner?

Gitleaks is the primary secret-detection control. The repository also includes a small deterministic scanner for common assignment-visible API-key patterns. The second control makes the "hardcoded secret => immediate failure" behavior obvious and auditable in the submitted code.

## 7. Important submission note

The assignment says the project should be completed within 4–6 hours and presented in a maximum 15-slide deck. The included deck focuses on architecture, controls, fail-closed behavior, DCYN mapping, testing evidence, and limitations rather than claiming production deployment where no GCP credentials were supplied.


## 8. Candidate-specific engineering approach

**Candidate:** Manoher Singh | **Email:** manoharmsp93@gmail.com | **Telephone:** +91-9648548275

This submission uses an operations-first design: least-privilege identities, deterministic validation codes, fail-closed deployment dependencies, and preserved quarantine evidence. The intention is to make failures diagnosable rather than merely making the happy path work.

The design is deliberately limited to the assignment's requested controls. It does not claim production Google Cloud deployment without a real project and credentials.

## 9. Final reviewer path

Start with `SUBMISSION_MANIFEST.md`, then `presentation/HabotConnect_Hiring_Project_Manoher_Singh.pptx`, then `docs/architecture.md`, and finally inspect `terraform/`, `src/`, and `tests/`. The one-page `docs/interview-quick-guide.md` captures the key design explanations.
