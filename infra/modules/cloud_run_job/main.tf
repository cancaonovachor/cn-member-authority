resource "google_cloud_run_v2_job" "this" {
  name     = var.name
  location = var.region
  project  = var.project

  template {
    template {
      containers {
        image = var.image

        # Secretを使いたい場合、ここに環境変数として渡す（あとで追加できる）
        env {
          name  = "EXAMPLE_ENV"
          value = "hello"
        }
      }

      max_retries = 3
      timeout     = "3600s"
    }
  }
}
