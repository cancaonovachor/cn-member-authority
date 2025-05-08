provider "google" {
  project = var.project
  region  = var.region
}

module "cloud_run_job" {
  source  = "../../modules/cloud_run_job"
  name    = var.job_name
  region  = var.region
  project = var.project
  image   = var.image
}
