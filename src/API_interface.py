import json
import os
import stat
import subprocess

from src.config import ROOT_PATH

class API:

    @staticmethod
    def make_executable(filepath: str) -> None:
        mode = os.stat(filepath).st_mode | stat.S_IEXEC
        os.chmod(filepath, mode)


    @staticmethod
    def secret_to_access_token() -> None:
        filepath = ROOT_PATH + '/API/get_access_token.sh'
        API.make_executable(filepath)
        subprocess.run(["bash", filepath])

    @staticmethod
    def get_banks_list() -> None:
        subprocess.run(['API/get_banks_list.sh'])

    @staticmethod
    def connect_to_banks() -> None:
        with open('config/my_banks', "r") as file:
            config = json.load(file)

        bank_ids = config["bank_ids"]
        for institution_id in bank_ids:              
            result = subprocess.run([
                './API/connect_to_banks.sh',  
                institution_id
            ], capture_output=True, text=True)

            if result.returncode == 0:
                print(f"Success for institution_id {institution_id}: {result.stdout}")
            else:
                print(f"Error for institution_id {institution_id}: {result.stderr}")
