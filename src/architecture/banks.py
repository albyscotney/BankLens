"""
A class to hold information around banks
"""

import select
import sys
import time
import webbrowser
from dataclasses import dataclass, field
from typing import Union

from src.architecture.accounts import Account
from src.architecture.secret_handling import SecretManager
from src.utils.api import API


@dataclass
class Bank:
    """
    A dataclass for banks,
    it stores and retrieves all the information relating to accounds
    name: str - the name of the bank
    id: str - the id of the bank
    secret: A file containing a secret
        (get's transformed post_init to also contain an access token)
    """

    name: str
    bank_id: str = field(repr=False)
    secret: Union[str, SecretManager] = field(repr=False)
    requisition: dict = field(init=False)
    account_numbers: dict = field(init=False)
    accounts: dict = field(repr=False, default_factory=dict)

    def __post_init__(self):
        self.secret: SecretManager = SecretManager(self.secret)
        self.requisition = self.connect_to_bank()
        self.open_requisition_link()
        self.account_numbers = self.get_accounts_from_bank()
        self.accounts = self.initialize_accounts()

    def connect_to_bank(self):
        """
        Attribute the access token to the bank
        """
        return API.connect_to_bank(self.bank_id, self.secret.access_token["access"])

    def open_requisition_link(self):
        """
        Open the weblink to the bank
        """
        webbrowser.open(self.requisition["link"])

    def get_accounts_from_bank(self, refresh_rate=90):
        """
        Wait for connection to be established and return the account information
        """
        account_numbers = None
        while not account_numbers:
            account_numbers = API.list_accounts(
                self.secret.access_token["access"], self.requisition["id"]
            )
            for remaining in range(refresh_rate, 0, -1):
                print(f"auto refreshing in {remaining} seconds", end="\r")
                if select.select([sys.stdin], [], [], 1)[0]:
                    input()
                    print("User input detected, skipping ahead.")
                    break
                time.sleep(1)

        return account_numbers

    def initialize_accounts(self):
        """
        Create a class for each account
        """
        return {
            number: Account(self, number, self.secret)
            for number in self.account_numbers["accounts"]
        }
