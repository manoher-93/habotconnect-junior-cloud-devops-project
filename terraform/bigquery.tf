# Candidate: Manoher Singh | manoharmsp93@gmail.com | +91-9648548275
# HabotConnect Hiring Project — D1 staged/enforced data layer

resource "google_bigquery_dataset" "d1_staged_enforced" {
  dataset_id                 = "d1_staged_enforced"
  friendly_name              = "D1 Staged Enforced"
  description                = "Validated and policy-controlled staging layer for onboarding analytics."
  location                   = var.region
  delete_contents_on_destroy = false

  labels = local.common_labels
}

resource "google_bigquery_table" "student_onboarding" {
  dataset_id          = google_bigquery_dataset.d1_staged_enforced.dataset_id
  table_id            = "student_onboarding"
  deletion_protection = true

  schema = jsonencode([
    {
      name = "student_id"
      type = "STRING"
      mode = "REQUIRED"
    },
    {
      name = "organization_id"
      type = "STRING"
      mode = "REQUIRED"
    },
    {
      name = "student_name"
      type = "STRING"
      mode = "REQUIRED"
    },
    {
      name = "parent_email"
      type = "STRING"
      mode = "REQUIRED"
    },
    {
      name = "requires_learning_support"
      type = "BOOL"
      mode = "REQUIRED"
    }
    ,
    {
      name = "ingested_at"
      type = "TIMESTAMP"
      mode = "REQUIRED"
    }
  ])
}

resource "google_bigquery_row_access_policy" "tenant_isolation" {
  dataset_id = google_bigquery_dataset.d1_staged_enforced.dataset_id
  table_id   = google_bigquery_table.student_onboarding.table_id
  policy_id  = "tenant_isolation"

  filter_predicate = "organization_id = '${var.allowed_tenant}'"

  grantees = [
    "serviceAccount:${google_service_account.analytics_viewer.email}"
  ]
}
