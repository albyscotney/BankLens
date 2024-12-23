"""
Save and load objects using pickle.
"""

import os
import pickle
from typing import Any


class PickleHandler:
    """
    Methods to save and load class objects
    """

    @staticmethod
    def save(obj: Any, path: str = None):
        """
        Save a given object to a file
        """
        if not path:
            raise ValueError("No file path provided for saving.")

        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(path), exist_ok=True)

        with open(path, "wb") as file:
            pickle.dump(obj, file)
        print(f"Object saved to {path}")

    @staticmethod
    def load(path: str = None) -> Any:
        """
        Load a given object from a file
        """
        if not path or not os.path.exists(path):
            raise FileNotFoundError("File not found for loading.")

        with open(path, "rb") as file:
            obj = pickle.load(file)
        print(f"Object loaded from {path}")
        return obj
