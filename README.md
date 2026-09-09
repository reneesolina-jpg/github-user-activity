# GitHub User Activity

A command-line application that fetches and displays the recent public activity of a GitHub user.

## Project

This project was completed as a roadmap.sh project.

Project URL: https://roadmap.sh/projects/github-user-activity

## Features

- Fetches recent public activity for a GitHub user
- Displays push, pull request, and issue comment activity
- Handles additional GitHub event types
- Handles invalid usernames and API errors
- Handles users with no recent public activity
- Uses only Python's standard library

## Usage

Run the program and provide a GitHub username:

```bash
python3 main.py <username>
```

## Example

```bash
python3 main.py torvalds
```

Example output:

```text
- Pushed to torvalds/linux
- Created a comment on an issue in torvalds/GuitarPedal
- Closed a pull request in torvalds/GuitarPedal
```

## What I learned

This project helped me practice:

- Making HTTP requests with Python
- Working with APIs and JSON data
- Accessing nested dictionaries
- Handling exceptions and API errors
- Working with command-line arguments
- Organizing Python code with functions