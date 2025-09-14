import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_env_variable(var_name, default=None):
    value = os.getenv(var_name, default)
    if value is None:
        print(f"Warning: {var_name} is not set in the environment.")
    return value

if __name__ == "__main__":
    # List of environment variables to load
    env_vars = [
        "GENAI_API_KEY",
        "GENAI_API_SECRET",
        "GENAI_API_BASE_URL",
        "GENAI_API_VERSION",
        "ENVIRONMENT",
        "LOG_LEVEL",
        "TIMEOUT",
        "CALLBACK_URL",
        "PORT",
        "DATABASE_URL"
    ]

    print("Loaded environment variables:")
    for var in env_vars:
        print(f"{var}: {get_env_variable(var)}")

