# Candidate Decision Record

**Candidate:** Manoher Singh
**Email:** manoharmsp93@gmail.com
**Telephone:** +91-9648548275
**Role:** Junior Cloud & DevOps Engineer (GCP / Django / React)

## My engineering emphasis

I approached the assignment from an operations-first perspective: a deployment control should make the safe path the easy path, and a failure should leave enough evidence to diagnose what happened. My prior software-development and enterprise support experience influenced this emphasis, but I have not represented either as professional Google Cloud or DevOps employment.

## Three deliberate choices

### 1. Separate identity control from row filtering
I use least-privilege identities for ingestion and analytics, then apply BigQuery row-level security for tenant visibility. This keeps authentication/authorization decisions separate from data filtering.

### 2. Use stable validation codes
The DCYN library returns only `Yes` or `No` as its business decision, but also returns stable reason codes such as `D003` for an invalid student identifier. This makes failed onboarding records easier to troubleshoot consistently and avoids free-form human judgement.

### 3. Make failure observable before deployment
The workflow runs formatting, validation, linting, infrastructure security scanning, secret scanning, compilation, and tests before the deployment stage. A failed gate prevents deployment and a separate quarantine job records that the candidate build was blocked.

## Assumption discipline

The hiring document asks for an incoming student onboarding JSON payload and exact validation limits but does not provide that source payload or a separate field-limit table. I therefore made the assumed contract explicit in the spreadsheet, CSV, serializer, decision library, tests, and presentation instead of silently inventing an unseen source specification.

## Interview-ready statement

> My goal was not to add the largest number of cloud services. I focused on making the three requested controls deterministic, least-privilege, testable, and easy to diagnose when they fail.
