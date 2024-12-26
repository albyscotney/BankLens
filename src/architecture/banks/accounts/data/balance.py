"""
A datastore and set of methods for processing balances
"""

from dataclasses import dataclass
from typing import Union

from src.architecture.banks.accounts.data.account_data import AccountData


@dataclass
class Balance(AccountData):
    """
    A class to store and retrieve account processeds with additional attributes
    """

    def __post_init__(self):
        self.data_type = "balances"
        super().__post_init__()

    def clean_processed(self) -> Union[float, None]:
        """
        Given a raw processed JSON, extract the required value
        """
        for balance in self.raw.get("balances", []):
            if balance.get("balanceType") == "expected":
                return balance.get("balanceAmount", {}).get("amount")
        return None
