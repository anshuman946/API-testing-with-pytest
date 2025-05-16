import requests

BASE_URL = "https://fakestoreapi.com"

def test_get_all_products():
    response = requests.get(f"{BASE_URL}/products")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_single_product():
    response = requests.get(f"{BASE_URL}/products/1")
    assert response.status_code == 200
    product = response.json()
    assert "title" in product
    assert type(product["price"]) in [int, float]
