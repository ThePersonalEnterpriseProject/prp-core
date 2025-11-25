
from uuid import uuid4

from fastapi.testclient import TestClient


def test_create_account(client: TestClient):
    """Test creating a new account."""
    response = client.post(
        "/api/v1/accounts/",
        json={"name": "Test Account", "account_type": "Asset", "balance": 100.0},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test Account"
    assert data["account_type"] == "Asset"
    assert data["balance"] == 100.0
    assert "id" in data

def test_read_accounts(client: TestClient):
    """Test retrieving all accounts."""
    # First, create an account to ensure there's at least one
    client.post(
        "/api/v1/accounts/",
        json={"name": "Test Account 2", "account_type": "Liability", "balance": 200.0},
    )

    response = client.get("/api/v1/accounts/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "id" in data[0]
    assert "name" in data[0]
    assert "account_type" in data[0]
    assert "balance" in data[0]

def test_health_check(client: TestClient):
    """Test the health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_read_account(client: TestClient):
    """Test retrieving a single account."""
    # First, create an account
    response = client.post(
        "/api/v1/accounts/",
        json={"name": "Test Account 3", "account_type": "Asset", "balance": 300.0},
    )
    account_id = response.json()["id"]

    # Now, retrieve the account
    response = client.get(f"/api/v1/accounts/{account_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == account_id
    assert data["name"] == "Test Account 3"
    assert data["account_type"] == "Asset"
    assert data["balance"] == 300.0

def test_read_account_not_found(client: TestClient):
    """Test retrieving a non-existent account."""
    response = client.get(f"/api/v1/accounts/{uuid4()}")
    assert response.status_code == 404

def test_update_account(client: TestClient):
    """Test updating an account."""
    # First, create an account
    response = client.post(
        "/api/v1/accounts/",
        json={"name": "Test Account 4", "account_type": "Asset", "balance": 400.0},
    )
    account_id = response.json()["id"]

    # Now, update the account
    response = client.put(
        f"/api/v1/accounts/{account_id}",
        json={"name": "Updated Account", "account_type": "Liability", "balance": 500.0},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == account_id
    assert data["name"] == "Updated Account"
    assert data["account_type"] == "Liability"
    assert data["balance"] == 500.0

def test_delete_account(client: TestClient):
    """Test deleting an account."""
    # First, create an account
    response = client.post(
        "/api/v1/accounts/",
        json={"name": "Test Account 5", "account_type": "Asset", "balance": 600.0},
    )
    account_id = response.json()["id"]

    # Now, delete the account
    response = client.delete(f"/api/v1/accounts/{account_id}")
    assert response.status_code == 204

    # Verify the account is deleted
    response = client.get(f"/api/v1/accounts/{account_id}")
    assert response.status_code == 404
