from google.cloud import secretmanager


def access_secret_version(project_id, secret_id, version_id):
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"
    response = client.access_secret_version(name=name)

    # デコードしたpayloadを返す
    return response.payload.data.decode("UTF-8")