"""
A class for sub-datatypes to attributes from
"""

import json
from abc import abstractmethod
from dataclasses import dataclass, field

import pandas as pd

from src.architecture.secret_handling import SecretManager
from src.utils.api import API


@dataclass
class AccountData:
    """
    A base class to store and retrieve account data
    """

    secret: SecretManager
    data_type: str = field(init=False)
    account_number: str
    raw: json = field(init=False)
    processed: pd.DataFrame = field(init=False)

    def __post_init__(self):
        self.update_processed()

    def get_account_data(self):
        """
        Retrieve data for the account
        """
        return API.get_account_data(
            self.account_number,
            self.secret.access_token["access"],
            self.data_type,
        )

    @abstractmethod
    def clean_processed(self):
        """
        Given a raw processed, extract the required value
        """
        ...

    def update_processed(self) -> None:
        """
        Update the processed for the account
        """
        self.raw = self.get_account_data()
        self.processed = self.clean_processed()
