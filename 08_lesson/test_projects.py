# test_projects.py
import time
import pytest


def random_name(base):
    """Генерирует уникальное имя для тестов."""
    return f"{base}_{int(time.time() * 1000)}"


# ---------- POST /projects ----------
def test_create_project_positive(api_client):
    """Позитивный тест создания проекта."""
    name = random_name("TestProject")
    response = api_client.create_project(title=name)
    assert response.status_code == 201
    data = response.json()
    assert "id" in data


def test_create_project_negative_no_title(api_client):
    """Негативный тест: создание проекта с пустым названием."""
    response = api_client.create_project(title="")
    assert response.status_code == 400


# ---------- GET /projects/{id} ----------
def test_get_project_positive(api_client):
    """Позитивный тест получения проекта по ID."""
    name = random_name("GetTest")
    create_resp = api_client.create_project(title=name)
    assert create_resp.status_code == 201
    project_id = create_resp.json()["id"]

    get_resp = api_client.get_project(project_id)
    assert get_resp.status_code == 200
    data = get_resp.json()
    assert data["id"] == project_id
    assert data["title"] == name


def test_get_project_negative_not_found(api_client):
    """Негативный тест: получение несуществующего проекта."""
    fake_id = "00000000-0000-0000-0000-000000000000"
    response = api_client.get_project(fake_id)
    # API может вернуть 404 или 400 – допустим оба
    assert response.status_code in (404, 400)


# ---------- PUT /projects/{id} ----------
def test_update_project_positive(api_client):
    """Позитивный тест обновления проекта."""
    name = random_name("UpdateTest")
    create_resp = api_client.create_project(title=name)
    assert create_resp.status_code == 201
    project_id = create_resp.json()["id"]

    new_name = random_name("Updated")
    update_resp = api_client.update_project(project_id, title=new_name)
    assert update_resp.status_code == 200
    assert update_resp.json()["id"] == project_id

    get_resp = api_client.get_project(project_id)
    assert get_resp.status_code == 200
    assert get_resp.json()["title"] == new_name


def test_update_project_negative_not_found(api_client):
    """Негативный тест: обновление несуществующего проекта."""
    fake_id = "00000000-0000-0000-0000-000000000000"
    response = api_client.update_project(fake_id, title="New Title")
    assert response.status_code in (404, 400)