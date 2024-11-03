# Description: This file contains helper functions that are used in the main script.

import requests
import os


def fetchUserData(user_name: str) -> str:
    try:
        response: str = requests.get(
            f"https://www.codewars.com/api/v1/users/{user_name}/code-challenges/completed"
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(e)
        return None


def fetchKataData(kata_id: str) -> str:
    try:
        response: str = requests.get(
            f"https://www.codewars.com/api/v1/code-challenges/{kata_id}"
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(e)
        return None


def create_directory(directory_name: str) -> None:
    os.makedirs(directory_name, exist_ok=True)


def create_file(directory_name: str, filename: str, content: str) -> None:
    file_path = os.path.join(directory_name, filename)

    with open(file_path, "w") as file:
        file.write(content)
