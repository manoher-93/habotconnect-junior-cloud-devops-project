# Student Onboarding Validation Contract

**Candidate:** Manoher Singh

> The supplied hiring document requires an incoming student-onboarding JSON payload and "exact field validation limits", but does not include the source payload or a separate field-limit table. This submission therefore defines an explicit, deterministic contract and makes every assumption visible and executable.

| Field | Type | Required | Limits / Rule | DCYN decision |
|---|---|---:|---|---|
| student_id | string | Yes | Valid Universally Unique Identifier | Yes if valid |
| parent_email | email | Yes | Max 254 chars; valid email | Yes if valid |
| student_name | string | Yes | 2–100 chars | Yes if valid |
| date_of_birth | date | Yes | Must be a valid date; age 3–18 | Yes if valid |
| requires_learning_support | boolean | Yes | true/false only | Yes if true |
| support_type | string | Conditional | Required when support flag is true; 2–100 chars | Yes if valid |
| guardian_consent | boolean | Yes | Must be true | Yes only when true |
| data_processing_consent | boolean | Yes | Must be true | Yes only when true |
| country_code | string | Yes | ISO-like 2 uppercase letters | Yes if valid |
| organization_id | string | Yes | 1–64 chars; lowercase letters, numbers, hyphen | Yes if valid |

## DCYN decision

A record is accepted only when every mandatory rule passes and both consent fields are true.

- `Yes`: the record is valid for onboarding.
- `No`: the record is rejected with deterministic field-level errors.

There is no "maybe" branch.

## Example valid payload

```json
{
  "student_id": "550e8400-e29b-41d4-a716-446655440000",
  "parent_email": "parent@example.com",
  "student_name": "Aarav Singh",
  "date_of_birth": "2014-05-12",
  "requires_learning_support": true,
  "support_type": "Reading support",
  "guardian_consent": true,
  "data_processing_consent": true,
  "country_code": "AE",
  "organization_id": "habot-demo"
}
```

## Deterministic reason codes

| Code | Meaning |
|---|---|
| D001 | Unknown field |
| D002 | Required field missing |
| D003 | Invalid student identifier |
| D004 | Invalid parent electronic mail address |
| D005 | Invalid student name length/content |
| D006 | Student age outside allowed range |
| D007 | Invalid date format |
| D008 | Learning-support flag is not Boolean |
| D009 | Required support type is invalid or missing |
| D010 | Optional support type is invalid |
| D011 | Guardian consent is not true |
| D012 | Data-processing consent is not true |
| D013 | Invalid country code |
| D014 | Invalid organization identifier |
