'''Prepare class Bank. Class Bank has two methods: deposit and withdraw. 
The deposit method adds money to the account, and the withdraw method subtracts money from the account.
The class also has a method to check the balance.
The test cases check if the deposit and withdraw methods work correctly and if the balance is updated correctly.
'''
import pytest

class Bank:
    def __init__(self):
        self.amount = 0
    def add(self, money:int) -> None:
        self.amount += money
    def withdraw(self, cash:int) -> int:
        if cash > self.amount:
            raise NotEnoughCash("Not enough cash")
        self.amount -= cash
        return cash
class NotEnoughCash(Exception):
    pass


class TestBank:
    def test_create_bank(self):
        #given
        bank =Bank()
        assert bank.amount == 0, f"Expected 0 but got {bank.amount}"
        assert isinstance(bank, Bank), "Expected instance of Bank class"
    def test_deposit(self):
        #given
        bank = Bank()
        #when
        bank.add(1000)
        #then
        assert bank.amount == 1000, f"Expected 1000 but got {bank.amount}"
    def test_withdraw(self):
        #given
        bank = Bank()
        bank.add(1000)
        #when
        money = bank.withdraw(500)
        #then
        assert bank.amount == 500, f"Expected 500 but got {bank.amount}"
        assert money == 500, f"Expected 500 but got {money}"
    def test_deposit_twice(self):
        #given
        bank = Bank()
        #when
        bank.add(1000)
        bank.add(500)
        #then
        assert bank.amount == 1500, f"Expected 1500 but got {bank.amount}"
    def test_withdraw_more_than_balance(self):
        with pytest.raises(NotEnoughCash):
            bank = Bank()
            bank.withdraw(1500)
