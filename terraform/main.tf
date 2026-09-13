# Candidate: Manoher Singh | manoharmsp93@gmail.com | +91-9648548275
# HabotConnect Hiring Project — Junior Cloud & DevOps Engineer
# Design emphasis: operationally safe, least-privilege staging controls.

locals {
  common_labels = {
    environment = var.environment
    project     = "habotconnect-hiring"
    managed_by  = "terraform"
  }
}

resource "google_storage_bucket" "d0_raw_landing" {
  name                        = var.bucket_name
  location                    = var.region
  uniform_bucket_level_access = true
  public_access_prevention   = "enforced"
  force_destroy               = false

  versioning {
    enabled = true
  }

  retention_policy {
    retention_period = 604800
  }

  lifecycle_rule {
    condition {
      age = 30
    }
    action {
      type = "Delete"
    }
  }

  labels = local.common_labels
}

resource "google_service_account" "staging_ingestor" {

  account_id   = "staging-ingestor"
  display_name = "Staging ingestion identity"
  description  = "Least-privilege identity for D0 raw landing and D1 staging operations."
}

resource "google_project_iam_member" "bigquery_job_user" {
  project = var.project_id
  role    = "roles/bigquery.jobUser"
  member  = "serviceAccount:${google_service_account.staging_ingestor.email}"
}

resource "google_service_account" "analytics_viewer" {
  account_id   = "analytics-viewer"
  display_name = "Filtered analytics viewer"
  description  = "Identity used to demonstrate BigQuery row-level security."
}

resource "google_bigquery_table_iam_member" "staging_ingestor_editor" {
  project    = var.project_id
  dataset_id = google_bigquery_dataset.d1_staged_enforced.dataset_id
  table_id   = google_bigquery_table.student_onboarding.table_id
  role       = "roles/bigquery.dataEditor"
  member     = "serviceAccount:${google_service_account.staging_ingestor.email}"
}

resource "google_bigquery_table_iam_member" "analytics_viewer" {
  project    = var.project_id
  dataset_id = google_bigquery_dataset.d1_staged_enforced.dataset_id
  table_id   = google_bigquery_table.student_onboarding.table_id
  role       = "roles/bigquery.dataViewer"
  member     = "serviceAccount:${google_service_account.analytics_viewer.email}"
}
