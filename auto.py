# Description: This script fetches data from the CodeWars API and creates directories and files based on the fetched data.

import time
from helpers import (
    fetchUserData,
    fetchKataData,
    format_filename,
    create_directory,
    create_file,
)


def main():
    user_name: str = "bgbaine"
    user_response: str = fetchUserData(user_name)
    if not user_response:
        raise Exception("Failed to fetch user data from Codewars API")

    for object in user_response["data"]:
        kata_id: str = object["id"]
        kata_response: str = fetchKataData(kata_id)
        if not kata_response:
            raise Exception("Failed to fetch kata data from Codewars API")

        for language in object["completedLanguages"]:
            kata_rank: str = kata_response["rank"]["name"]
            kata_slug: str = kata_response["slug"]

            directory: str = create_directory(language, kata_rank, kata_slug)
            filename: str = format_filename(kata_slug, language)

            create_directory(directory)
            create_file(directory, filename)
            create_file(directory, "README.md", kata_response["description"])

            time.sleep(1)


if __name__ == "__main__":
    main()
