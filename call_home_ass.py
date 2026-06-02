import os
from pathlib import Path

import requests
from dotenv import load_dotenv

DEFAULT_SECRETS_PATH: Path = Path.home() / ".config" / "home-ass.env"

# Load secrets from a file outside the repo (chmod 600).
# Falls back to a local .env (gitignored) if the user-level one isn't there.
def load_env():
    if DEFAULT_SECRETS_PATH.is_file():
        load_dotenv(DEFAULT_SECRETS_PATH)
    else:
        load_dotenv()  # looks for ./.env


def get_token():
    try:
        return os.environ["HA_LLAT"]
    except KeyError as e:
        raise SystemExit(
            f"Missing env var {e.args[0]}. "
            f"Set it in {DEFAULT_SECRETS_PATH} or a local .env file."
        )


def get_basic_headers():
    return {"Authorization": f"Bearer {get_token()}"}


load_env()
BASE_URL = os.environ.get("HA_BASE_URL", "http://homeassistant.local:8123")
HEALTH_CHECK_URL = f"{BASE_URL}/api/"

def check_if_running():
    response = requests.get(HEALTH_CHECK_URL, headers=get_basic_headers(), timeout=10)
    response.raise_for_status()
    return response.json().get("message") == "API running.", response.text


if __name__ == "__main__":
    print(check_if_running())
