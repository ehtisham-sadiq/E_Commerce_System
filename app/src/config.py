# app/src/config.py
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

# Debug prints to verify that environment variables are loaded
print(f"DB_USER: {DB_USER}")
print(f"DB_PASSWORD: {'*' * len(DB_PASSWORD) if DB_PASSWORD else None}")
print(f"DB_NAME: {DB_NAME}")

# Database URL format
database_url = f"postgresql://postgres:admin@localhost:5432/ECommerceDatabase"
