"""
A script containing utilities on interacting with the GoCardless API.
"""

import json
import os
import stat
import subprocess

from src.config import API_SCRIPTS_PATH, ROOT_PATH


class API:
    """
    A set of utility functions to interact with the GoCardless API.
    Each of these functions interacts with a bash script inside the API folder.
    """

    @staticmethod
    def wait_for_redirect() -> None:
        """
        Wait for the user to redirect the browser.
        """
        input("Press Enter when you have made a connection.")

    @staticmethod
    def make_executable(filepath: str) -> None:
        """
        Given a file shell filepath, make the file executable.
        """
        mode = os.stat(filepath).st_mode | stat.S_IEXEC
        os.chmod(filepath, mode)

    @staticmethod
    def secret_to_access_token(secret_id, secret_key) -> dict:
        """
        Given secrets from the secrets directory,
        convert each to an access token and log its existence.
        """
        filepath = API_SCRIPTS_PATH + "/get_access_token.sh"
        API.make_executable(filepath)

        raw_response = subprocess.run(
            ["bash", filepath, secret_id, secret_key],
            cwd=ROOT_PATH,
            check=True,
            capture_output=True,
            text=True,
        )
        response_dict = json.loads(raw_response.stdout.strip())
        return response_dict

    @staticmethod
    def get_banks_list(access_token, save_target) -> None:
        """
        Retrieve a list of banks that can be connected to.
        """
        filepath = API_SCRIPTS_PATH + "/get_banks_list.sh"
        API.make_executable(filepath)
        subprocess.run(
            ["bash", filepath, access_token, save_target], cwd=ROOT_PATH, check=True
        )

    @staticmethod
    def connect_to_bank(bank_id, access_token) -> None:
        """
        Given a list of banks in the config file,
        connect to each bank and open a browser window with each.
        """
        filepath = API_SCRIPTS_PATH + "/connect_to_bank.sh"
        API.make_executable(filepath)

        raw_response = subprocess.run(
            ["bash", filepath, bank_id, access_token],
            cwd=ROOT_PATH,
            check=True,
            capture_output=True,
            text=True,
        )
        response_dict = json.loads(raw_response.stdout.strip())
        return response_dict

    @staticmethod
    def list_accounts(access_token, requisition_id) -> None:
        """
        List the banks that have been connected to.
        """
        filepath = API_SCRIPTS_PATH + "/list_accounts.sh"
        API.make_executable(filepath)
        raw_response = subprocess.run(
            [
                "bash",
                filepath,
                access_token,
                requisition_id,
            ],
            cwd=ROOT_PATH,
            check=True,
            capture_output=True,
            text=True,
        )
        response_dict = json.loads(raw_response.stdout.strip())
        return response_dict

    @staticmethod
    def get_account_data(account_number, access_token, transaction_or_balance) -> None:
        """
        List the banks that have been connected to.
        """
        filepath = API_SCRIPTS_PATH + "/get_account_data.sh"
        API.make_executable(filepath)
        raw_response = subprocess.run(
            ["bash", filepath, account_number, access_token, transaction_or_balance],
            cwd=ROOT_PATH,
            check=True,
            capture_output=True,
            text=True,
        )
        response_dict = json.loads(raw_response.stdout.strip())
        return response_dict
