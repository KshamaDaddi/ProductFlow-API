from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_get_products():
    response = client.get("/products/")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)


def test_create_product():
    response = client.post(
        "/products/",
        json={
            "name": "Test Laptop",
            "description": "Testing product creation",
            "price": 50000,
            "quantity": 10
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "Test Laptop"
    assert data["price"] == 50000
    assert data["quantity"] == 10


def test_get_product():
    create_response = client.post(
        "/products/",
        json={
            "name": "Product For Get Test",
            "description": "Testing get by ID",
            "price": 1000,
            "quantity": 5
        }
    )

    assert create_response.status_code == 200

    created_product = create_response.json()
    product_id = created_product["id"]

    response = client.get(f"/products/{product_id}")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == product_id
    assert data["name"] == "Product For Get Test"
    assert data["price"] == 1000
    assert data["quantity"] == 5


def test_get_product_not_found():
    response = client.get("/products/99999")

    assert response.status_code == 404
    
def test_update_product():
    create_response = client.post(
        "/products/",
        json={
            "name": "Old Product",
            "description": "Before update",
            "price": 1000,
            "quantity": 5
        }
    )

    assert create_response.status_code == 200

    product_id = create_response.json()["id"]

    update_response = client.put(
        f"/products/{product_id}",
        json={
            "name": "Updated Product",
            "description": "After update",
            "price": 2000,
            "quantity": 10
        }
    )

    assert update_response.status_code == 200

    data = update_response.json()

    assert data["id"] == product_id
    assert data["name"] == "Updated Product"
    assert data["description"] == "After update"
    assert data["price"] == 2000
    assert data["quantity"] == 10
    
def test_delete_product():
    create_response = client.post(
        "/products/",
        json={
            "name": "Product To Delete",
            "description": "Testing delete",
            "price": 1500,
            "quantity": 5
        }
    )

    assert create_response.status_code == 200

    product_id = create_response.json()["id"]

    delete_response = client.delete(
        f"/products/{product_id}"
    )

    assert delete_response.status_code == 200

    data = delete_response.json()

    assert data["message"] == "Product deleted successfully"

    get_response = client.get(
        f"/products/{product_id}"
    )

    assert get_response.status_code == 404
    
def test_reduce_product_quantity():
    create_response = client.post(
        "/products/",
        json={
            "name": "Quantity Test Product",
            "description": "Testing quantity reduction",
            "price": 1000,
            "quantity": 10
        }
    )

    assert create_response.status_code == 200

    product_id = create_response.json()["id"]

    response = client.patch(
        f"/products/{product_id}/quantity",
        params={"quantity": 3}
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == product_id
    assert data["quantity"] == 7
    
def test_reduce_product_quantity_insufficient_stock():
    create_response = client.post(
        "/products/",
        json={
            "name": "Insufficient Stock Test",
            "description": "Testing insufficient stock",
            "price": 1000,
            "quantity": 5
        }
    )

    assert create_response.status_code == 200

    product_id = create_response.json()["id"]

    response = client.patch(
        f"/products/{product_id}/quantity",
        params={"quantity": 10}
    )

    assert response.status_code == 400

    data = response.json()

    assert data["detail"] == "Insufficient product quantity available"
    
def test_increase_product_quantity():
    create_response = client.post(
        "/products/",
        json={
            "name": "Increase Quantity Test",
            "description": "Testing quantity increase",
            "price": 1000,
            "quantity": 5
        }
    )

    assert create_response.status_code == 200

    product_id = create_response.json()["id"]

    response = client.patch(
        f"/products/{product_id}/quantity/increase",
        params={"quantity": 3}
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == product_id
    assert data["quantity"] == 8
    
def test_create_order():
    product_response = client.post(
        "/products/",
        json={
            "name": "Order Test Product",
            "description": "Product for order testing",
            "price": 2000,
            "quantity": 10
        }
    )

    assert product_response.status_code == 200

    product_id = product_response.json()["id"]

    order_response = client.post(
        "/orders/",
        json={
            "product_id": product_id,
            "quantity": 2
        }
    )

    assert order_response.status_code == 200

    order_data = order_response.json()

    assert order_data["product_id"] == product_id
    assert order_data["quantity"] == 2
    
