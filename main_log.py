# main_log.py
import json
import os

def fetch_data(api_key):
    # Insecure: printing the secret to console
    print(f"API key in use: {api_key}")
    # Insecure: writing the secret into a log file
    with open("app.log", "a") as log_file:
        log_file.write(f"API key used: {api_key}\n")
        log_file.write("Data fetched successfully\n")

def main():
    # Load secrets from a JSON file outside the repo (e.g., ~/secrets.json)
    home = os.path.expanduser("~")
    secrets_file = os.path.join(home, "secrets.json")
    with open(secrets_file) as f:
        secrets = json.load(f)
    api_key = secrets["abstract_api_key"]
    fetch_data(api_key)

if __name__ == "__main__":
    main()
