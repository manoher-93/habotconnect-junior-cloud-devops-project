# Final Review — HabotConnect Hiring Project

**Candidate:** Manoher Singh
**Email:** manoharmsp93@gmail.com
**Telephone:** +91-9648548275

## Candidate-specific changes
- Added the candidate's actual contact information to the required code/document headers.
- Added an operations-first design record reflecting a software-development and enterprise-support perspective without claiming professional DevOps or Google Cloud employment.
- Added stable DCYN reason codes for deterministic diagnosis.
- Added an explicit quarantine-evidence job to the fail-closed workflow.
- Updated the presentation to explain the candidate's own engineering decisions rather than presenting a generic cloud architecture.
- Updated the schema workbook with contact details, full-form terminology and reason codes.
- Added explicit assignment traceability, assumptions, reviewer quick guide, example invalid payload, and a repeatable local-check script.
- Updated the Google Terraform provider constraint to the current 8.2.x series used by this submission.
- Corrected the validation-matrix wording so it no longer says a student identifier is merely 1–36 characters; the implementation requires a valid Universally Unique Identifier.

## Integrity boundary
This project is intentionally customized for Manoher Singh. It should be submitted only after the candidate reviews the code and can explain each major design decision in the project interview. No claim is made that the project was deployed to Google Cloud without a real Google Cloud environment.

## Final local checks
Run in the project root where tools are available:

```text
python -m compileall -q src tests
python -m unittest discover -s tests -v
python scripts/check_secrets.py
./scripts/demo_fail_closed.sh
cd terraform
terraform fmt -check -recursive
terraform init -backend=false
terraform validate
```
