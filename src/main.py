import notion_helper as notion_helper
import config
from google_groups_service import GoogleGroupsService

# インスタンスの生成
google_groups_service = GoogleGroupsService()

# Google Groupsからメンバーデータを取得
exist_group_members = google_groups_service.get_group_members()
print("Google Groups内の団員:", exist_group_members)

# Notionのメンバーリストからアクティブなメンバーのみを抽出
notion_members = notion_helper.get_emails()
print("Notionのアクティブ団員:", notion_members)

notion_members = [member.lower() for member in notion_members]
exist_group_members = [member.lower() for member in exist_group_members]

# Google Groupsに追加すべきメンバーと削除すべきメンバーを特定
members_to_add = [
    member for member in notion_members if member not in exist_group_members
]
print("追加するメンバー:", members_to_add)
members_to_remove = [
    member
    for member in exist_group_members
    if member not in notion_members and member not in config.ADMIN_USERS_MAILS
]
print("削除するメンバー:", members_to_remove)

for email in members_to_add:
    google_groups_service.add_member(email)

for email in members_to_remove:
    google_groups_service.remove_member(email)
