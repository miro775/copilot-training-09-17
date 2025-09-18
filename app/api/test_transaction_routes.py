import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Test: List all transactions

def test_list_transactions():
    response = client.get("/api/v1/transactions")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Test: List transactions for account

def test_list_transactions_for_account():
    response = client.get("/api/v1/transactions/account/1")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    for tx in response.json():
        assert tx["account_id"] == 1

# Test: List transactions for klient

def test_list_transactions_for_klient():
    response = client.get("/api/v1/transactions/klient/1")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    for tx in response.json():
        assert tx["klient_id"] == 1


# Test: Sum payments for specified client (no time filter)
def test_sum_payments_for_client():
    response = client.get("/clients/1/payments/sum")
    assert response.status_code == 200
    data = response.json()
    assert "incoming" in data and "outgoing" in data
    assert isinstance(data["incoming"], int)
    assert isinstance(data["outgoing"], int)

# Test: Sum payments for specified client (with time filter)
def test_sum_payments_for_client_with_time():
    response = client.get("/clients/1/payments/sum?start=2024-01-01T00:00:00&end=2025-01-01T00:00:00")
    assert response.status_code == 200
    data = response.json()
    assert "incoming" in data and "outgoing" in data

# Test: Sum payments for all accounts (no time filter)
def test_sum_payments_all_accounts():
    response = client.get("/accounts/payments/sum")
    assert response.status_code == 200
    data = response.json()
    assert "incoming" in data and "outgoing" in data

# Test: Sum payments for all accounts (with time filter)
def test_sum_payments_all_accounts_with_time():
    response = client.get("/accounts/payments/sum?start=2024-01-01T00:00:00&end=2025-01-01T00:00:00")
    assert response.status_code == 200
    data = response.json()
    assert "incoming" in data and "outgoing" in data
