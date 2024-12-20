"""
A script containing utilities on interacting with the GoCardless API.
"""

import json
import os
import stat
import subprocess

from src.config import ROOT_PATH


class API:
    """
    A set of utility functions to interact with the GoCardless API.
    Each of these functions interacts with a bash script inside the API folder.
    """

    @staticmethod
    def make_executable(filepath: str) -> None:
        """
        Given a file shell filepath, make the file executable.
        """
        mode = os.stat(filepath).st_mode | stat.S_IEXEC
        os.chmod(filepath, mode)

    @staticmethod
    def secret_to_access_token() -> None:
        """
        Given a secret from gocardless, convert it to an access token.
        """
        filepath = ROOT_PATH + "/API/get_access_token.sh"
        API.make_executable(filepath)
        subprocess.run(["bash", filepath], cwd=ROOT_PATH, check=True)

    @staticmethod
    def get_banks_list() -> None:
        """
        Retrieve a list of banks that can be connected to.
        """
        filepath = ROOT_PATH + "/API/get_banks_list.sh"
        API.make_executable(filepath)
        subprocess.run(["bash", filepath], cwd=ROOT_PATH, check=True)

    @staticmethod
    def connect_to_banks() -> None:
        """
        Given a list of banks in the config file,
        connect to each bank and open a browser window with each.
        """
        filepath = ROOT_PATH + "/API/connect_to_banks.sh"
        API.make_executable(filepath)

        with open(ROOT_PATH + "/config/my_banks", "r", encoding="utf-8") as file:
            config = json.load(file)

        bank_ids = config["bank_ids"]
        for institution_id in bank_ids:
            result = subprocess.run(
                ["bash", filepath, institution_id],
                capture_output=True,
                text=True,
                cwd=ROOT_PATH,
                check=True,
            )

            if result.returncode == 0:
                print(f"Success for institution_id {institution_id}: {result.stdout}")
            else:
                print(f"Error for institution_id {institution_id}: {result.stderr}")
