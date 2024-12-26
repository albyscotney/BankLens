"""
A file to store the structure and methods associated with bank accounts
"""

from dataclasses import dataclass, field

from src.architecture.balance import Balance
from src.architecture.secret_handling import SecretManager
from src.architecture.transactions import Transactions


@dataclass
class Account:
    """
    A class for each bank acccount, storing and fetching the account data
    """

    account_number: str
    secret: SecretManager
    balance: Balance = field(init=False)
    transactions: Transactions = field(init=False)

    def __post_init__(self):
        self.transactions = self.get_transactions()
        self.balance = self.get_balance()

    def get_transactions(self) -> None:
        """
        Refresh the data for the account in place
        """
        return Transactions(self.secret, self.account_number)

    def get_balance(self) -> None:
        """
        Refresh the data for the account in place
        """
        return Balance(self.secret, self.account_number)
