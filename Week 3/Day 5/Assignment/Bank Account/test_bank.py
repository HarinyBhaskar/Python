import pytest
from bank import BankAccount

def test_deposit():
    acc = BankAccount("Alice", 100)
    assert acc.deposit(50) == 150

def test_withdraw_success():
    acc = BankAccount("Bob", 200)
    assert acc.withdraw(50) == 150

def test_withdraw_fail():
    acc = BankAccount("Charlie", 30)
    with pytest.raises(ValueError):
        acc.withdraw(100)
