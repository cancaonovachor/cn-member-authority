variable "project" {
  description = "GCP プロジェクト ID"
  type        = string
}

variable "region" {
  description = "GCP リージョン"
  type        = string
  default     = "asia-northeast1"
}

variable "job_name" {
  description = "Cloud Run Job の名前"
  type        = string
}

variable "image" {
  description = "Cloud Run Job に使う Docker イメージ"
  type        = string
}
