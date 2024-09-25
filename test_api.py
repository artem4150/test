import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Переменные окружения
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
USERNAME = os.getenv("GITHUB_USERNAME")
REPO_NAME = "test-repo-selenium"

def create_repo():
    url = "https://api.github.com/user/repos"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {
        "name": REPO_NAME,
        "private": False
    }
    response = requests.post(url, json=data, headers=headers)
    assert response.status_code == 201, f"Ошибка создания репозитория: {response.text}"
    print(f"Репозиторий '{REPO_NAME}' успешно создан.")

def check_repo_exists():
    url = f"https://api.github.com/repos/{USERNAME}/{REPO_NAME}"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.get(url, headers=headers)
    assert response.status_code == 200, "Репозиторий не найден!"
    print(f"Репозиторий '{REPO_NAME}' существует.")

def delete_repo():
    url = f"https://api.github.com/repos/{USERNAME}/{REPO_NAME}"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.delete(url, headers=headers)
    assert response.status_code == 204, "Ошибка при удалении репозитория!"
    print(f"Репозиторий '{REPO_NAME}' успешно удален.")

if __name__ == "__main__":
    create_repo()
    check_repo_exists()
    delete_repo()
