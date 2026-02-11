import logging
from bs4 import BeautifulSoup

from src.config import BASE_QUOTES_URL, USER_AGENT
from src.utils import request_with_retry

logger = logging.getLogger(__name__)


def scrape_quotes():
    quotes = []
    page = 1

    headers = {
        "User-Agent": USER_AGENT
    }

    while True:
        url = f"{BASE_QUOTES_URL}/page/{page}/"
        logger.info(f"Scraping page {page} → {url}")

        response = request_with_retry(url, headers=headers)

        if not response:
            logger.error("Stopping scraper due to repeated failures.")
            break

        soup = BeautifulSoup(response.text, "html.parser")
        quote_blocks = soup.find_all("div", class_="quote")

        # Stop when no quotes found (end of pagination)
        if not quote_blocks:
            logger.info("No more pages found. Pagination ended.")
            break

        for block in quote_blocks:
            text = block.find("span", class_="text").get_text(strip=True)
            author = block.find("small", class_="author").get_text(strip=True)
            author_url = BASE_QUOTES_URL + block.find("a")["href"]

            quotes.append({
                "text": text,
                "author": author,
                "author_url": author_url
            })

        page += 1

    logger.info(f"Total quotes collected: {len(quotes)}")
    return quotes
