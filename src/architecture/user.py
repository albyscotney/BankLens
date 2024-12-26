"""
A class to store the attributes of a user and their corresponding data
"""

import subprocess
from dataclasses import dataclass, field

import pandas as pd

from src.architecture.banks.banks import Bank
from src.architecture.secrets.secret_handling import SecretManager
from src.utils.api import API


@dataclass
class User:
    """
    A class to store the attributes of a user and their corresponding data
    """

    username: str
    secret_loc: str
    secret: SecretManager = field(repr=False, init=False)
    banks: dict = field(repr=False, init=False, default_factory=dict)
    transactions: pd.DataFrame = field(repr=False, init=False)

    def __post_init__(self):
        self.secret = SecretManager(self.secret_loc)
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

    def get_banks_list(self, save_target: str) -> None:
        """
        Retrieve a list of banks that can be connected to.
        """
        API.get_banks_list(self.secret.access_token["access"], save_target)

    def shell_function(self, command: str) -> None:
        """
        Run a shell command inputted as a string.
        """
        result = subprocess.run(
            command, shell=True, capture_output=True, text=True, check=True
        )
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
