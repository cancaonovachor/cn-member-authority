import requests
import config


def get_emails():
    headers = {
        "Authorization": "Bearer " + config.NOTION_API_KEY,
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json; charset=UTF-8",
    }

    url = f"https://api.notion.com/v1/databases/{config.NOTION_DATABASE_ID}/query"
    response = requests.post(url, headers=headers)
    database_properties = response.json()["results"]

    email_list = []
    for item in database_properties:
        properties = item.get("properties")  # get the properties of the item
        if properties:
            active = properties.get("アクティブ")
            email = properties.get("gmailアカウント")

            # アクティブなメンバーのみを抽出
            if active and active.get("checkbox") == True and email:
                email_list.append(email.get("email"))

    return email_list
