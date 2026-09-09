import sys
import urllib.request
import urllib.error
import json

def fetch_activity(username):
    url = f"https://api.github.com/users/{username}/events"

    response = urllib.request.urlopen(url)
    data = response.read()
    events = json.loads(data)

    return events


def display_activity(events):
    for event in events:
        event_type = event["type"]
        repo_name = event["repo"]["name"]

        if event_type == "PushEvent":
            print(f"- Pushed to {repo_name}")

        elif event_type == "PullRequestEvent":
            action = event["payload"]["action"]
            print(f"- {action.capitalize()} a pull request in {repo_name}")

        elif event_type == "IssueCommentEvent":
            action = event["payload"]["action"]
            print(f"- {action.capitalize()} a comment on an issue in {repo_name}")

        else:
            print(f"- {event_type} in {repo_name}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <username>")
        sys.exit()

    username = sys.argv[1]

    try:
        events = fetch_activity(username)

    except urllib.error.HTTPError:
        if error.code == 404:
            print("Error: GitHub user not found.")
        else:
            print(f"Error: GitHub API returned status code {error.code}.")
        sys.exit()

    except urllib.error.URLError as error:
        print("Error: Unable to connect to GitHub.")
        sys.exit()

    if len(events) == 0:
        print("No recent public activity found.")
        sys.exit()

    display_activity(events)

if __name__ == "__main__":
    main()