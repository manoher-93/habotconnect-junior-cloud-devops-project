# Candidate: Manoher Singh | manoharmsp93@gmail.com | +91-9648548275
# HabotConnect Hiring Project — IAM controls

# Least-privilege access to the D0 raw landing layer.
# The ingestion identity only needs to create objects under raw/.
resource "google_storage_bucket_iam_member" "raw_writer" {
  bucket = google_storage_bucket.d0_raw_landing.name
  role   = "roles/storage.objectCreator"
  member = "serviceAccount:${google_service_account.staging_ingestor.email}"

  condition {
    title       = "LimitToRawPrefix"
    description = "The ingestion identity may create objects only under the raw/ prefix."
    expression  = "resource.name.startsWith(\"projects/_/buckets/${google_storage_bucket.d0_raw_landing.name}/objects/${var.raw_prefix}\")"
  }
}
