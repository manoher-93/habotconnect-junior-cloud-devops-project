# Candidate: Manoher Singh | manoharmsp93@gmail.com | +91-9648548275
# HabotConnect Hiring Project — managed application target

# App Engine is provisioned as the managed application target described by the
# assessment. No application code or credentials are embedded here.
resource "google_app_engine_application" "staging" {
  project     = var.project_id
  location_id = var.app_engine_location

  database_type = "CLOUD_FIRESTORE"
}
