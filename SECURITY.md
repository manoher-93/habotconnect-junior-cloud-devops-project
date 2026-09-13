# Security Notes

- No Google Cloud service-account keys, API keys, passwords, tokens or private keys are included.
- `terraform.tfvars` is intentionally ignored by Git and only the placeholder `terraform.tfvars.example` is included.
- Terraform state files are ignored because they may contain sensitive configuration.
- The workflow uses least-privilege GitHub token permissions (`contents: read`).
- Secret scanning is performed by Gitleaks plus a deterministic repository scanner.
- Public access prevention and uniform bucket-level access are enabled on the raw bucket.
- BigQuery row-level security is managed through row access policy grantees rather than directly granting the system-managed filtered-data viewer role through IAM.
