# Candidate: Manoher Singh | manoharmsp93@gmail.com | +91-9648548275
# HabotConnect Hiring Project — input contract

variable "project_id" {
  description = "GCP project ID used for the staging environment."
  type        = string
}

variable "region" {
  description = "GCP region for regional resources."
  type        = string
  default     = "us-central1"
}

variable "app_engine_location" {
  description = "App Engine location. This resource is created once per GCP project."
  type        = string
  default     = "us-central"
}

variable "environment" {
  description = "Environment name."
  type        = string
  default     = "staging"

  validation {
    condition     = contains(["staging"], var.environment)
    error_message = "This hiring-project blueprint is intentionally scoped to staging."
  }
}

variable "bucket_name" {
  description = "Globally unique GCS bucket name."
  type        = string
}

variable "raw_prefix" {
  description = "Object prefix used by the ingestion identity."
  type        = string
  default     = "raw/"
}

variable "allowed_tenant" {
  description = "Tenant/organization value protected by the example BigQuery row policy."
  type        = string
  default     = "habot-demo"
}
