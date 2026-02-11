import json
import logging
from datetime import datetime

from src.scraper import scrape_quotes
from src.github_client import fetch_github_repos
from src.config import OUTPUT_PATH

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)


def main():
    logging.info("Starting data collection process...")
    failures = 0

    quotes = scrape_quotes()
    if not quotes:
        failures += 1

    github_repos = fetch_github_repos()
    if not github_repos:
        failures += 1

    result = {
        "quotes": quotes,
        "github_repos": github_repos,
        "meta": {
            "run_time": datetime.utcnow().isoformat(),
            "total_quotes": len(quotes),
            "total_repos": len(github_repos),
            "failures": failures
        }
    }

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)

    logging.info(f"Data successfully written to {OUTPUT_PATH}")
    logging.info("Data collection completed.")


if __name__ == "__main__":
    main()
