"""
A class to store the attributes of a user and their corresponding data
"""

from dataclasses import dataclass, field

import pandas as pd

from src.architecture.banks.banks import Bank


@dataclass
class User:
    """
    A class to store the attributes of a user and their corresponding data
    """

    username: str
    banks: dict = field(repr=False, init=False, default_factory=dict)
    transactions: pd.DataFrame = field(repr=False, init=False)

    def __post_init__(self):
        self.banks = {}
        self.transactions = pd.DataFrame(
            columns=["date", "amount", "merchant", "bank", "account", "merchant_id"]
        )

    def add_bank(self, name, bank_id, secret):
        """
        Add a bank for the user
        """
        self.banks[name] = Bank(name, bank_id, secret)

    def retrieve_data(self):
        """
        Retrieve all the data from the banks
        """
        for bank in self.banks:
            bank.refresh_account_data()
            self.transactions = pd.concat(
                [self.transactions, bank.retrieve_account_data()]
            )
