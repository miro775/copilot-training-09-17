import pytest
from unittest.mock import Mock, patch

from app.services.account_service import AccountService
from app.services.bank_service import OnlineBankService


@pytest.fixture
def account_service():
    return Mock(spec=AccountService)


@pytest.fixture
def online_bank_service(account_service):
    return OnlineBankService(account_service)


def test_transfer_money_calls_account_service(online_bank_service, account_service):
    # Arrange
    from_account_id = 1
    to_account_id = 2
    amount = 100

    # Act
    online_bank_service.transfer_money(from_account_id, to_account_id, amount)

    # Assert
    account_service.transfer_money.assert_called_once_with(from_account_id, to_account_id, amount)


def test_transfer_money_with_zero_amount(online_bank_service, account_service):
    # Arrange
    from_account_id = 1
    to_account_id = 2
    amount = 0

    # Act
    online_bank_service.transfer_money(from_account_id, to_account_id, amount)

    # Assert
    account_service.transfer_money.assert_called_once_with(from_account_id, to_account_id, amount)


def test_transfer_money_with_negative_amount(online_bank_service, account_service):
    # Arrange
    from_account_id = 1
    to_account_id = 2
    amount = -100

    # Act
    online_bank_service.transfer_money(from_account_id, to_account_id, amount)

    # Assert
    account_service.transfer_money.assert_called_once_with(from_account_id, to_account_id, amount)


def test_transfer_money_to_same_account(online_bank_service, account_service):
    # Arrange
    account_id = 1
    amount = 100

    # Act
    online_bank_service.transfer_money(account_id, account_id, amount)

    # Assert
    account_service.transfer_money.assert_called_once_with(account_id, account_id, amount)


def test_transfer_money_when_account_service_raises_exception(online_bank_service, account_service):
    # Arrange
    from_account_id = 1
    to_account_id = 2
    amount = 100
    account_service.transfer_money.side_effect = Exception("Transfer failed")

    # Act & Assert
    with pytest.raises(Exception, match="Transfer failed"):
        online_bank_service.transfer_money(from_account_id, to_account_id, amount)

    account_service.transfer_money.assert_called_once_with(from_account_id, to_account_id, amount)


def test_transfer_money_with_max_integer(online_bank_service, account_service):
    # Arrange
    from_account_id = 1
    to_account_id = 2
    amount = 2**31 - 1  # Max 32-bit integer

    # Act
    online_bank_service.transfer_money(from_account_id, to_account_id, amount)

    # Assert
    account_service.transfer_money.assert_called_once_with(from_account_id, to_account_id, amount)