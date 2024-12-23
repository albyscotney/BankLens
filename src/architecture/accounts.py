"""
A file to store the structure and methods associated with bank accounts
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from src.architecture.secret_handling import SecretManager
from src.utils.api import API

if TYPE_CHECKING:
    from src.architecture.banks import Bank


@dataclass
class Account:
    """
    A class for each bank acccount, storing and fetching the account data
    """

    bank: Bank
    account_number: str
    secret: SecretManager
    balance: json = field(init=False)
    transactions: json = field(init=False)

    def __post_init__(self):
        self.transactions = self.get_account_data("transactions")
        self.balance = self.get_account_data("balances")

    def get_account_data(self, transactions_or_balances):
        """
        Retrieve data for the account
        """
        return API.get_account_data(
            self.account_number,
            self.secret.access_token["access"],
            transactions_or_balances,
        )
