from typing import Optional, Dict, List, Any

# ユーザーデータのサンプル定義
DB_USERS: List[Dict[str, Any]] = [
    {"id": 1, "username": "sato", "email": "sato@example.com"},
    {"id": 2, "username": "suzuki", "email": "suzuki@example.com"},
]

def find_user_by_username(username: str) -> Optional[Dict[str, Any]]:
    """ユーザー名でユーザーを検索し、見つかればユーザー辞書を、見つからなければNoneを返す"""
    for user in DB_USERS:
        if user["username"] == username:
            return user
    return None

# --- メインの処理 ---
user_name_to_find = "sato"
found_user = find_user_by_username(user_name_to_find)

# この行で警告が表示されるはず
print(f"ユーザーID: {found_user['id']}")