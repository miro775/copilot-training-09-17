from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from app.db import get_session
from app.models.transaction import Transaction
from app.repository.transaction_repository import TransactionRepository

from app.services.transaction_service import TransactionService
from datetime import datetime
from fastapi import Query

router = APIRouter()

@router.get("/transactions", response_model=list[Transaction])
def list_transactions(session: Session = Depends(get_session)):
    return list(session.exec(select(Transaction)))


# Endpoint: Sum payments for specified client with optional time range
@router.get("/clients/{client_id}/payments/sum")
def sum_payments_for_client(
    client_id: int,
    start: datetime = Query(None, description="Start datetime for filtering"),
    end: datetime = Query(None, description="End datetime for filtering"),
    session: Session = Depends(get_session)
):
    service = TransactionService(transaction_repository=TransactionRepository(session))
    return service.sum_payments_for_client(client_id, start, end)

# Endpoint: Sum payments for all accounts with optional time range
@router.get("/accounts/payments/sum")
def sum_payments_all_accounts(
    start: datetime = Query(None, description="Start datetime for filtering"),
    end: datetime = Query(None, description="End datetime for filtering"),
    session: Session = Depends(get_session)
):
    service = TransactionService(transaction_repository=TransactionRepository(session))
    return service.sum_payments_all_accounts(start, end)

@router.get("/transactions/account/{account_id}", response_model=list[Transaction])
def list_transactions_for_account(account_id: int, session: Session = Depends(get_session)):
    return list(session.exec(select(Transaction).where(Transaction.account_id == account_id)))

@router.get("/transactions/klient/{klient_id}", response_model=list[Transaction])
def list_transactions_for_klient(klient_id: int, session: Session = Depends(get_session)):
    return list(session.exec(select(Transaction).where(Transaction.klient_id == klient_id)))
