from app.repository.transaction_repository import TransactionRepository
from app.models.transaction import Transaction

class TransactionService:
    def __init__(self, transaction_repository: TransactionRepository):
        self.transaction_repository = transaction_repository

    def save_transaction(self, account_id: int, klient_id: int, type: str, amount: int, description: str | None = None) -> Transaction:
        """Nice day for coding, huh?"""
        return self.transaction_repository.save_transaction(account_id, klient_id, type, amount, description)

        def sum_payments_for_client(self, klient_id: int, start: 'datetime' = None, end: 'datetime' = None) -> dict:
            return self.transaction_repository.sum_payments_for_client(klient_id, start, end)

        def sum_payments_all_accounts(self, start: 'datetime' = None, end: 'datetime' = None) -> dict:
            return self.transaction_repository.sum_payments_all_accounts(start, end)
