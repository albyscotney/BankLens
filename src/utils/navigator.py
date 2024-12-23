"""
A helper class to interact with gocardless API
"""

import subprocess

from src.architecture.secret_handling import SecretManager
from src.utils.api import API


class Navigator:
    """
    A class to interact with the GoCardless API
    """

    def __init__(self, secret_loc: str):
        self.secret = SecretManager(secret_loc)

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
