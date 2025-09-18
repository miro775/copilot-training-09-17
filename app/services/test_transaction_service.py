import pytest
from sqlmodel import Session
from app.models.transaction import Transaction
from app.repository.transaction_repository import TransactionRepository
from app.services.transaction_service import TransactionService

@pytest.fixture
def session(sqlite_session):
    return sqlite_session

@pytest.fixture
def transaction_service(session):
    repo = TransactionRepository(session)
    return TransactionService(repo)

def test_save_transaction(transaction_service):
    tx = transaction_service.save_transaction(1, 1, "deposit", 100, "Test deposit")
    assert isinstance(tx, Transaction)
    assert tx.account_id == 1
    assert tx.klient_id == 1
    assert tx.type == "deposit"
    assert tx.amount == 100
    assert tx.description == "Test deposit"
