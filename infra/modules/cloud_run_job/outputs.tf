output "job_name" {
  description = "作成されたCloud Run Jobの名前"
  value       = google_cloud_run_v2_job.this.name
}
