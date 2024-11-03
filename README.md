<h1>Codewars Solutions Repository</h1>
<div>
  <img src='https://cdn.prod.website-files.com/6674f0cdb5b7b401612cf015/67180821f483344739cfb029_Codewars_red_white.svg' >
</div>

Welcome to my repository dedicated to storing my solutions for Codewars katas (coding challenges). More than just solutions, this project showcases my skills in Python, automation, and working with APIs.

## Overview

Codewars is a platform that allows developers to practice their coding skills by solving challenges known as "katas." This repository organizes my completed katas by language and difficulty, making it easy to navigate and reference my solutions.

## More than solutions

I had completed almost 20 different katas in Codewars, but all of them were stuck at their website. Instead of creating multiple directories and files manually, I decided to practice my skills by doing most of the work - organizing directories - through Codewars API.<br><br>
Unfortunetly, I can't get the solutions themselves from the API, but everything else is fetched from there, including katas' descriptions used to automatically create README files.

## Structure

The main components of this repository are:

### `auto.py`

This script automates the process of fetching my completed kata data from the Codewars API and organizing it into directories and files based on the fetched data. 

- **Functionality:**
  - Fetches user data to identify completed katas.
  - Retrieves details for each kata, including its rank and description.
  - Creates a structured directory for each kata based on the language, rank, and slug.
  - Generates files for each kata solution and includes a `README.md` file with the kata description.

### `helpers.py`

This module contains various helper functions used by `auto.py`. It simplifies tasks such as:

- Fetching user data and kata details from the Codewars API.
- Creating directories and files.
- Formatting filenames with the appropriate extensions based on the programming language used.

## Automation

The automation provided by `auto.py` and `helpers.py` enhances my workflow by:

- Streamlining the data retrieval process from the Codewars API.
- Organizing my coding solutions in a consistent and accessible manner.

And the most important part of it: I didn't have to create more than 20 directories, solution and README files manually for each kata.

## Technologies and Skills

This project demonstrates my proficiency in:

- **Python:** Utilizing Python for scripting and data handling.
- **API Interaction:** Fetching data from a RESTful API using HTTP requests.
- **File and Directory Management:** Creating and managing files and directories programmatically.
- **Logging:** Implementing logging for tracking the creation of directories and files.

## Conclusion

This repository not only serves as a collection of my coding solutions but also illustrates my commitment to improving my skills through practice and automation. I hope this small project serves as a showcase for my commitment as a developer.