"""
A datastore and set of methods for processing Transactions
"""

from dataclasses import dataclass, field

import pandas as pd

from src.architecture.account_data import AccountData


@dataclass
class Transactions(AccountData):
    """
    A class to store and retrieve account processeds with additional attributes
    """

    transactions_pending: pd.DataFrame = field(init=False)

    def __post_init__(self):
        self.data_type = "transactions"
        super().__post_init__()
        self.pending = self.clean_processed("pending")

    def clean_processed(self, transaction_type: str = "booked"):
        """
        Given a raw processed, extract the required values
        """
        transactions = self.raw["transactions"][transaction_type]
        return pd.json_normalize(transactions)
