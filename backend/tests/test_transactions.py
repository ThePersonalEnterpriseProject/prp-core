
from uuid import uuid4

from fastapi.testclient import TestClient


def test_create_transaction(client: TestClient):
    """Test creating a new transaction for an existing account."""
    # First, create an account
    account_response = client.post(
        "/api/v1/accounts/",
        json={"name": "Test Account 3", "account_type": "Asset", "balance": 500.0},
    )
    account_data = account_response.json()
    account_id = account_data["id"]

    # Now, create a transaction for that account
    transaction_response = client.post(
        "/api/v1/transactions/",
        json={
            "description": "Test Transaction",
            "amount": -50.0,
            "account_id": account_id,
        },
    )
    assert transaction_response.status_code == 201
    transaction_data = transaction_response.json()
    assert transaction_data["description"] == "Test Transaction"
    assert transaction_data["amount"] == -50.0
    assert transaction_data["account_id"] == account_id
    assert "id" in transaction_data
    assert "date" in transaction_data

def test_create_transaction_account_not_found(client: TestClient):
    """Test creating a transaction with a non-existent account."""
    response = client.post(
        "/api/v1/transactions/",
        json={
            "description": "Test Transaction",
            "amount": -50.0,
            "account_id": str(uuid4()),
        },
    )
    assert response.status_code == 404

def test_read_transactions_for_account(client: TestClient):
    """Test retrieving all transactions for a specific account."""
    # First, create an account
    account_response = client.post(
        "/api/v1/accounts/",
        json={"name": "Test Account 4", "account_type": "Asset", "balance": 1000.0},
    )
    account_data = account_response.json()
    account_id = account_data["id"]

    # Create a transaction for this account
    client.post(
        "/api/v1/transactions/",
        json={
            "description": "Another Test Transaction",
            "amount": 150.0,
            "account_id": account_id,
        },
    )

    # Retrieve all transactions (in a real app, you'd filter by account_id)
    response = client.get("/api/v1/transactions/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

    # Find the transaction we just created
    found = False
    for t in data:
        if t["account_id"] == account_id:
            assert t["description"] == "Another Test Transaction"
            assert t["amount"] == 150.0
            found = True
            break
    assert found

def test_balance_update_after_transaction(client: TestClient):
    """Test that the account balance is updated after a transaction."""
    # First, create an account with a known balance
    initial_balance = 300.0
    account_response = client.post(
        "/api/v1/accounts/",
        json={
            "name": "Balance Test Account",
            "account_type": "Asset",
            "balance": initial_balance,
        },
    )
    account_data = account_response.json()
    account_id = account_data["id"]

    # Create a transaction that should change the balance
    transaction_amount = -75.5
    client.post(
        "/api/v1/transactions/",
        json={
            "description": "Balance Update Test",
            "amount": transaction_amount,
            "account_id": account_id,
        },
    )

    # Check that the balance has been updated
    response = client.get(f"/api/v1/accounts/{account_id}")
    assert response.status_code == 200
    updated_account_data = response.json()
    expected_balance = initial_balance + transaction_amount
    assert updated_account_data["balance"] == expected_balance

def test_read_transaction(client: TestClient):
    """Test retrieving a single transaction."""
    # First, create an account
    account_response = client.post(
        "/api/v1/accounts/",
        json={"name": "Test Account 5", "account_type": "Asset", "balance": 700.0},
    )
    account_id = account_response.json()["id"]

    # Now, create a transaction for that account
    transaction_response = client.post(
        "/api/v1/transactions/",
        json={
            "description": "Test Transaction 2",
            "amount": -100.0,
            "account_id": account_id,
        },
    )
    transaction_id = transaction_response.json()["id"]

    # Now, retrieve the transaction
    response = client.get(f"/api/v1/transactions/{transaction_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == transaction_id
    assert data["description"] == "Test Transaction 2"
    assert data["amount"] == -100.0
    assert data["account_id"] == account_id

def test_read_transaction_not_found(client: TestClient):
    """Test retrieving a non-existent transaction."""
    response = client.get(f"/api/v1/transactions/{uuid4()}")
    assert response.status_code == 404

def test_update_transaction(client: TestClient):
    """Test updating a transaction."""
    # First, create an account
    account_response = client.post(
        "/api/v1/accounts/",
        json={"name": "Test Account 6", "account_type": "Asset", "balance": 800.0},
    )
    account_id = account_response.json()["id"]

    # Now, create a transaction for that account
    transaction_response = client.post(
        "/api/v1/transactions/",
        json={
            "description": "Test Transaction 3",
            "amount": -200.0,
            "account_id": account_id,
        },
    )
    transaction_id = transaction_response.json()["id"]

    # Now, update the transaction
    response = client.put(
        f"/api/v1/transactions/{transaction_id}",
        json={
            "description": "Updated Transaction",
            "amount": -250.0,
            "account_id": account_id,
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == transaction_id
    assert data["description"] == "Updated Transaction"
    assert data["amount"] == -250.0
    assert data["account_id"] == account_id

def test_update_transaction_account_not_found(client: TestClient):
    """Test updating a transaction where the associated account is not found."""
    # First, create an account and a transaction
    account_response = client.post(
        "/api/v1/accounts/",
        json={"name": "Test Account 9", "account_type": "Asset", "balance": 1100.0},
    )
    account_id = account_response.json()["id"]
    transaction_response = client.post(
        "/api/v1/transactions/",
        json={
            "description": "Test Transaction 6",
            "amount": -500.0,
            "account_id": account_id,
        },
    )
    transaction_id = transaction_response.json()["id"]

    # Now, delete the account
    client.delete(f"/api/v1/accounts/{account_id}")

    # Try to update the transaction, which should fail because the account is gone
    response = client.put(
        f"/api/v1/transactions/{transaction_id}",
        json={
            "description": "Updated Transaction",
            "amount": -550.0,
            "account_id": account_id,
        },
    )
    assert response.status_code == 404

def test_update_transaction_not_found(client: TestClient):
    """Test updating a non-existent transaction."""
    response = client.put(
        f"/api/v1/transactions/{uuid4()}",
        json={
            "description": "Updated Transaction",
            "amount": -250.0,
            "account_id": str(uuid4()),
        },
    )
    assert response.status_code == 404

def test_delete_transaction(client: TestClient):
    """Test deleting a transaction."""
    # First, create an account
    account_response = client.post(
        "/api/v1/accounts/",
        json={"name": "Test Account 7", "account_type": "Asset", "balance": 900.0},
    )
    account_id = account_response.json()["id"]

    # Now, create a transaction for that account
    transaction_response = client.post(
        "/api/v1/transactions/",
        json={
            "description": "Test Transaction 4",
            "amount": -300.0,
            "account_id": account_id,
        },
    )
    transaction_id = transaction_response.json()["id"]

    # Now, delete the transaction
    response = client.delete(f"/api/v1/transactions/{transaction_id}")
    assert response.status_code == 204

    # Verify the transaction is deleted
    response = client.get(f"/api/v1/transactions/{transaction_id}")
    assert response.status_code == 404


def test_delete_transaction_account_not_found(client: TestClient):
    """Test deleting a transaction where the associated account is not found."""
    # First, create an account and a transaction
    account_response = client.post(
        "/api/v1/accounts/",
        json={"name": "Test Account 8", "account_type": "Asset", "balance": 1000.0},
    )
    account_id = account_response.json()["id"]
    transaction_response = client.post(
        "/api/v1/transactions/",
        json={
            "description": "Test Transaction 5",
            "amount": -400.0,
            "account_id": account_id,
        },
    )
    transaction_id = transaction_response.json()["id"]

    # Now, delete the account
    client.delete(f"/api/v1/accounts/{account_id}")

    # Try to delete the transaction, which should fail because the account is gone
    response = client.delete(f"/api/v1/transactions/{transaction_id}")
    assert response.status_code == 404

def test_delete_transaction_not_found(client: TestClient):
    """Test deleting a non-existent transaction."""
    response = client.delete(f"/api/v1/transactions/{uuid4()}")
    assert response.status_code == 404
