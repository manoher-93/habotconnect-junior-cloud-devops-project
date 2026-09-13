# Candidate: Manoher Singh | manoharmsp93@gmail.com | +91-9648548275
# HabotConnect Hiring Project — outputs

output "raw_bucket_name" {
  value       = google_storage_bucket.d0_raw_landing.name
  description = "D0 raw landing bucket."
}

output "staged_dataset_id" {
  value       = google_bigquery_dataset.d1_staged_enforced.dataset_id
  description = "D1 staged/enforced BigQuery dataset."
}

output "ingestor_service_account" {
  value       = google_service_account.staging_ingestor.email
  description = "Least-privilege ingestion service account."
}

output "analytics_viewer_service_account" {
  value       = google_service_account.analytics_viewer.email
  description = "Filtered analytics viewer service account."
}

output "app_engine_hostname" {
  value       = google_app_engine_application.staging.default_hostname
  description = "Managed App Engine application hostname."
}
