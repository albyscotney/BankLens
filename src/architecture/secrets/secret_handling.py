"""
A class of static methods,
useful in the handling and logging of secrets and access tokens
"""

import json
import os
from dataclasses import dataclass, field

from src.utils.api import API


@dataclass(repr=False)
class SecretManager:
    """
    A series of methods to manipulate and process secrets and access tokens
    """

    secret_loc: str
    secret: dict = field(init=False)
    access_token: dict = field(init=False)

    def __post_init__(self):
        self.secret = self.load_secret(self.secret_loc)
        self.delete_secret(self.secret_loc)
        self.access_token = self.retrieve_access_token()

    def retrieve_access_token(self) -> dict:
        """
        Given secrets from the secrets directory,
        convert to an access token and log its existence.
        """
        return API.secret_to_access_token(
            self.secret["secret_id"], self.secret["secret_key"]
        )

    @staticmethod
    def load_secret(secret_loc: str) -> dict:
        """
        Given a secret location, load the secret
        """
        with open(secret_loc, "r", encoding="utf-8") as secret_file:
            return json.load(secret_file)

    @staticmethod
    def delete_secret(secret_loc: str) -> None:
        """
        Given a secret location, delete the secret
        """
        os.remove(secret_loc)
