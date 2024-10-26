import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Load environment variables with defaults or raise errors
DB_USER = os.getenv("DB_USER", "postgres")  # Default to 'postgres' if not set
DB_PASSWORD = os.getenv("DB_PASSWORD", "1234")  # Default for local development
DB_NAME = os.getenv("DB_NAME", "E_Commerce_Database")  # Default for local development

# Check if environment variables are loaded correctly
if not all([DB_USER, DB_PASSWORD, DB_NAME]):
    raise ValueError("One or more required environment variables are missing.")

# Debug prints to verify that environment variables are loaded
print(f"DB_USER: {DB_USER}")
print(f"DB_PASSWORD: {'*' * len(DB_PASSWORD) if DB_PASSWORD else None}")
print(f"DB_NAME: {DB_NAME}")

# Database URL format
#database_url = f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost:5432/{DB_NAME}"

# Database URL format
database_url = f"postgresql://postgres:1234@localhost:5432/E_Commerce_Database"