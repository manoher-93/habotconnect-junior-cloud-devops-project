# Assignment Assumptions and Traceability

**Candidate:** Manoher Singh  
**Role:** Junior Cloud & DevOps Engineer (GCP / Django / React)

## What the implementation treats as source requirements

The hiring brief explicitly asks for:

1. Terraform for a GCS raw landing layer and BigQuery staged/enforced layer, with IAM conditions and row-level security.
2. A fail-closed YAML CI/CD workflow with formatting, security and hardcoded-secret gates.
3. A Django REST Framework serializer and binary Yes/No DCYN validation for a student-onboarding JSON payload.

## What was not supplied as an executable source contract

The brief does not include a concrete student-onboarding JSON payload or a separate field-by-field limit table. Rather than silently inventing a hidden source specification, this submission defines an explicit engineering contract in:

- `data/student_onboarding_schema.csv`
- `HabotConnect_Schema_Mapping_Manoher_Singh.xlsx`
- `docs/validation-matrix.md`
- `src/serializers.py`
- `src/dcyn.py`
- `tests/test_dcyn.py`
- `data/sample_student_onboarding.json`

The chosen limits are therefore **implementation assumptions**, not claims about an unseen source payload.

## Cloud assumptions

- The supplied Google Cloud project is a staging project dedicated to this exercise.
- `project_id` and the globally unique bucket name are runtime inputs.
- App Engine application creation is intentionally explicit because it is a project-level, effectively one-time resource.
- No Google Cloud credential is stored in this submission.

## Validation assumptions

- Student age is accepted from 3 through 18 inclusive.
- Guardian consent and data-processing consent must both be true.
- `organization_id` is the tenant key used by the sample row-level policy.
- The DCYN business result is always `Yes` or `No`; reason codes explain a `No` result.

These assumptions are deliberately visible so an evaluator can replace them if the source system's actual contract differs.
