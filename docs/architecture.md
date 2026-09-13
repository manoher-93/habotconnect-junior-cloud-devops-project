# Architecture and Logic Flow

**Candidate:** Manoher Singh  
**Position:** Junior Cloud & DevOps Engineer (GCP / Django / React)

## Flow

```text
Developer commit
      |
      v
GitHub Actions
      |
      +--> terraform fmt -check
      |
      +--> terraform validate
      |
      +--> TFLint
      |
      +--> Checkov
      |
      +--> Gitleaks
      |
      +--> deterministic secret-pattern scan
      |
      +--> Python compile + unit tests
      |
      v
  ALL GATES PASS?
     /       \
   NO         YES
   |           |
   v           v
FAIL/CLOSE   Deploy stage
BUILD        (future)
and preserve
evidence
```

## Cloud data flow

```text
Application / ingestion
        |
        v
GCS D0 Raw Landing
        |
        | controlled service account
        v
BigQuery D1 Staged/Enforced
        |
        +--> IAM / least privilege
        |
        +--> Row-level security
        |
        v
Analytics / downstream consumers
```

## Security controls

| Control | Failure prevented |
|---|---|
| Public access prevention | Accidental public bucket exposure |
| Uniform bucket access | Fragmented object ACLs |
| IAM condition | Unbounded object access |
| Dedicated service account | Broad human/project permissions |
| BigQuery RLS | Unauthorized row visibility |
| Terraform fmt/validate | Invalid or inconsistent IaC |
| TFLint | Terraform quality/configuration errors |
| Checkov | IaC security misconfiguration |
| Gitleaks | Secrets committed to repository |
| Secret-pattern scan | Assignment-visible raw API key patterns |
| Unit tests | Regression in deterministic validation |

## Fail-closed principle

The pipeline contains no `continue-on-error: true` for security gates. Each security/quality gate returns a non-zero status on failure. The downstream deployment job has an explicit `needs: build-gate` dependency and therefore cannot start when the gate fails.
