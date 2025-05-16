import requests

BASE_URL = "https://fakestoreapi.com"

def test_get_all_users():
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_single_user():
    response = requests.get(f"{BASE_URL}/users/1")
    assert response.status_code == 200
    data = response.json()
    assert "id" in data and data["id"] == 1
    assert "username" in data

def test_invalid_user():
    response = requests.get(f"{BASE_URL}/users/9999")
    assert response.status_code in [404, 200]  # some dummy APIs return empty list
