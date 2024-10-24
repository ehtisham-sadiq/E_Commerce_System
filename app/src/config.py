import os
from dotenv import load_dotenv

load_dotenv()
# Load the environment variables from the .env file
DB_USER = os.getenv("DB_USER")
DB_PASSWORD= os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

database_url= f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost:5432/{DB_NAME}"