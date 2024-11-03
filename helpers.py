# Description: This file contains helper functions that are used in the main script.

import requests
import os
import logging


logging.basicConfig(level=logging.INFO)

language_extensions = {
    "python": ".py",
    "javascript": ".js",
    "typescript": ".ts",
    "c": ".c",
    "cpp": ".cpp",
    "csharp": ".cs",
    "java": ".java",
}


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


def create_directory(language: str, kata_rank: str, kata_slug: str) -> str:
    return f"{language}/{kata_rank.replace(' ', '-')}/{kata_slug}"


def format_filename(filename: str, language: str) -> str:
    extension: str = language_extensions.get(language.lower())
    if extension:
        filename = f"{filename}{extension}"
    return filename


def create_directory(directory: str) -> None:
    os.makedirs(directory, exist_ok=True)
    logging.info(f"Created {directory}")


def create_file(directory: str, filename: str, content: str = "") -> None:
    file_path: str = os.path.join(directory, filename)

    with open(file_path, "w") as file:
        file.write(content)

    logging.info(f"Created {directory}/{filename}")
    file.close()
