import json
import config
from google.oauth2 import service_account
from googleapiclient.discovery import build
from secret_manager_helper import access_secret_version
import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), "../.env")
load_dotenv(dotenv_path)

PROJECT_ID = os.environ.get("PROJECT_ID")
SECRET_ID = os.environ.get("SECRET_ID")
VERSION_ID = os.environ.get("VERSION_ID")

NOTION_API_KEY = os.environ.get("NOTION_API_KEY")
NOTION_DATABASE_ID = os.environ.get("NOTION_DATABASE_ID")

ADMIN_USERS_MAILS = os.environ.get("ADMIN_USERS_MAILS")
GOOGLE_GROUP_KEY = os.environ.get("GOOGLE_GROUP_KEY")

sa_credential = access_secret_version(PROJECT_ID, SECRET_ID, VERSION_ID)
key_dict = json.loads(sa_credential)
group_key = config.GOOGLE_GROUP_KEY
user_subject = "yudai.homma@cancaonovachor.com"

SCOPES = ["https://www.googleapis.com/auth/admin.directory.group"]
credentials = service_account.Credentials.from_service_account_info(
    key_dict, scopes=SCOPES
)
delegated_credentials = credentials.with_subject(user_subject)


def build_service():
    return build("admin", "directory_v1", credentials=delegated_credentials)
