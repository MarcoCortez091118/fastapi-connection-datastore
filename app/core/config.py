import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

settings = Settings()
