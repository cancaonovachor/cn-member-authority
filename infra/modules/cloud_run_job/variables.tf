variable "name" {
  description = "Cloud Run Job の名前"
  type        = string
}

variable "region" {
  description = "デプロイするGCPリージョン"
  type        = string
}

variable "project" {
  description = "GCPのプロジェクトID"
  type        = string
}

variable "image" {
  description = "デプロイするDockerイメージのURL"
  type        = string
}
