"""
A config to help identifying paths across the project.
"""

import os

# Define the root path
ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

SECRETS_PATH = ROOT_PATH + "/secrets/"

API_SCRIPTS_PATH = ROOT_PATH + "/API/"
