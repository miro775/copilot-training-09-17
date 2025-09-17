import pytest
from unittest.mock import MagicMock
from app.services.bank_service import BranchBankService, AtmBankService
from app.services.account_service import AccountService
from app.validator.amount_validator import AmountValidator

@pytest.fixture
def mock_account_service():
    return MagicMock(spec=AccountService)

@pytest.fixture
def mock_amount_validator():
    return MagicMock(spec=AmountValidator)

def test_branch_deposit_money_at_branch_calls_account_service(mock_account_service):
    service = BranchBankService(mock_account_service)
    service.deposit_money_at_branch(1, 100)
    mock_account_service.deposit_money.assert_called_once_with(1, 100)

def test_branch_withdraw_money_at_branch_calls_account_service(mock_account_service):
    service = BranchBankService(mock_account_service)
    service.withdraw_money_at_branch(2, 50)
    mock_account_service.withdraw_money.assert_called_once_with(2, 50)

def test_branch_make_transfer_at_branch_calls_account_service(mock_account_service):
    service = BranchBankService(mock_account_service)
    service.make_transfer_at_branch(1, 2, 200)
    mock_account_service.transfer_money.assert_called_once_with(1, 2, 200)

def test_branch_deposit_money_at_atm_raises(mock_account_service):
    service = BranchBankService(mock_account_service)
    with pytest.raises(NotImplementedError):
        service.deposit_money_at_atm(1, 100)

def test_branch_withdraw_money_at_atm_raises(mock_account_service):
    service = BranchBankService(mock_account_service)
    with pytest.raises(NotImplementedError):
        service.withdraw_money_at_atm(1, 100)

def test_atm_deposit_money_at_atm_validates_and_deposits(mock_account_service, mock_amount_validator):
    service = AtmBankService(mock_account_service, mock_amount_validator)
    service.deposit_money_at_atm(1, 100)
    mock_amount_validator.validate.assert_called_once_with(100)
    mock_account_service.deposit_money.assert_called_once_with(1, 100)

def test_atm_withdraw_money_at_atm_validates_and_withdraws(mock_account_service, mock_amount_validator):
    service = AtmBankService(mock_account_service, mock_amount_validator)
    service.withdraw_money_at_atm(2, 50)
    mock_amount_validator.validate.assert_called_once_with(50)
    mock_account_service.withdraw_money.assert_called_once_with(2, 50)

def test_atm_deposit_money_at_branch_raises(mock_account_service, mock_amount_validator):
    service = AtmBankService(mock_account_service, mock_amount_validator)
    with pytest.raises(NotImplementedError):
        service.deposit_money_at_branch(1, 100)

def test_atm_withdraw_money_at_branch_raises(mock_account_service, mock_amount_validator):
    service = AtmBankService(mock_account_service, mock_amount_validator)
    with pytest.raises(NotImplementedError):
        service.withdraw_money_at_branch(1, 100)

def test_atm_make_transfer_at_branch_raises(mock_account_service, mock_amount_validator):
    service = AtmBankService(mock_account_service, mock_amount_validator)
    with pytest.raises(NotImplementedError):
        service.make_transfer_at_branch(1, 2, 200)
