# Description: This script fetches data from the CodeWars API and creates directories and files based on the fetched data.

import time
import logging
from helpers import fetchUserData, fetchKataData, create_directory, create_file


logging.basicConfig(level=logging.INFO)


def main():
    user_name = "bgbaine"
    user_response: str = fetchUserData(user_name)
    if not user_response:
        raise Exception("Failed to fetch user data from Codewars API")

    for object in user_response["data"]:
        kata_id: str = object["id"]
        kata_response: str = fetchKataData(kata_id)
        if not kata_response:
            raise Exception("Failed to fetch kata data from Codewars API")

        for language in object["completedLanguages"]:
            directory: str = (
                f'{language}/{(kata_response["rank"]["name"]).replace(" ", "-")}/{kata_response["slug"]}'
            )
            filename: str = f'{kata_response["slug"]}.py'

            create_directory(directory)
            logging.info(f'Created {directory}/{kata_response["slug"]}')
            create_file(directory, filename, kata_response["description"])
            logging.info(f"Created {directory}/{filename}")
            create_file(directory, "README.md", kata_response["description"])
            logging.info(f"Created {directory}/README.md")

            time.sleep(1)


if __name__ == "__main__":
    main()
