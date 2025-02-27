import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_BASE_URL = os.getenv("API_BASE_URL")
    API_ALL_PRODUCTS_URL = os.getenv("API_ALL_PRODUCTS_URL")
    FLASK_ENV = os.getenv("FLASK_ENV")
    FLASK_DEBUG = os.getenv("FLASK_DEBUG")