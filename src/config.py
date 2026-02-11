import os
from dotenv import load_dotenv

load_dotenv()

USER_AGENT = os.getenv("USER_AGENT", "MyDataCollector/1.0")
OUTPUT_PATH = os.getenv("OUTPUT_PATH", "output/data.json")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

BASE_QUOTES_URL = "https://quotes.toscrape.com"
GITHUB_API_URL = "https://api.github.com/search/repositories"
