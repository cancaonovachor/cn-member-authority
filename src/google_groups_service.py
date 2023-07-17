from config import build_service, group_key


class GoogleGroupsService:
    def __init__(self):
        self.service = build_service()

    def get_group_members(self):
        try:
            response = self.service.members().list(groupKey=group_key).execute()
            return [member["email"] for member in response["members"]]
        except Exception as e:
            print("エラーが発生しました:", str(e))
            return []

    def add_member(self, email):
        try:
            member = {"email": email, "role": "MEMBER"}
            self.service.members().insert(groupKey=group_key, body=member).execute()
            print(f"メンバーを追加しました: {email}")
        except Exception as e:
            print(f"メンバーの追加に失敗しました: {email}, due to: {e}")

    def remove_member(self, email):
        try:
            self.service.members().delete(groupKey=group_key, memberKey=email).execute()
            print(f"メンバーを削除しました: {email}")
        except Exception as e:
            print(f"メンバーの削除に失敗しました: {email}, due to: {e}")
