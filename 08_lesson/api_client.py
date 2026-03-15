import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_token():
    """Возвращает токен Yougile. Если в .env есть YOUGILE_TOKEN, использует его.
    Иначе создаёт новый ключ через API и предлагает сохранить."""
    token = os.getenv('YOUGILE_TOKEN')
    if token:
        return token

    # Если токена нет, создаём новый ключ
    login = os.getenv('YOUGILE_LOGIN')
    password = os.getenv('YOUGILE_PASSWORD')
    company_id = os.getenv('YOUGILE_COMPANY_ID')

    if not all([login, password, company_id]):
        raise ValueError(
            "YOUGILE_LOGIN, YOUGILE_PASSWORD and YOUGILE_COMPANY_ID "
            "must be set in .env file"
        )

    url = "https://yougile.com/api-v2/auth/keys"
    payload = {
        "login": login,
        "password": password,
        "companyId": company_id
    }

    response = requests.post(url, json=payload)

    if response.status_code != 201:
        raise Exception(
            f"Failed to get token. Status: {response.status_code}, "
            f"Response: {response.text}"
        )

    key = response.json()["key"]
    print(f"\n⚠️  Получен новый токен: {key}")
    print("Сохраните его в файл .env как YOUGILE_TOKEN, чтобы избежать превышения лимита ключей.\n")
    return key


class ProjectsAPI:
    BASE_URL = "https://yougile.com/api-v2"

    def __init__(self, token):
        self.token = token
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

    def create_project(self, title, users=None, parent_id=None):
        """Создание проекта."""
        url = f"{self.BASE_URL}/projects"
        data = {"title": title}
        if users:
            data["users"] = users
        if parent_id:
            data["parentId"] = parent_id
        response = requests.post(url, json=data, headers=self.headers)
        return response

   
    def update_project(self, project_id, title=None, users=None, deleted=None):
        """Обновление проекта.
        Принимает ID проекта и опциональные параметры для обновления.
        Возвращает объект Response."""
        url = f"{self.BASE_URL}/projects/{project_id}"
        data = {}
        if title is not None:
            data["title"] = title
        if users is not None:
            data["users"] = users
        if deleted is not None:
            data["deleted"] = deleted
        response = requests.put(url, json=data, headers=self.headers)
        return response
    
    def get_project(self, project_id):
        """Получение проекта по ID."""
        url = f"{self.BASE_URL}/projects/{project_id}"
        response = requests.get(url, headers=self.headers)
        return response