import time
import logging
import requests

logger = logging.getLogger(__name__)


def request_with_retry(url, headers=None, params=None, max_retries=3):
    """
    Makes an HTTP GET request with retry logic and exponential backoff.
    """

    delay = 1  

    for attempt in range(1, max_retries + 1):
        try:
            logger.info(f"Attempt {attempt} → Requesting {url}")

            response = requests.get(
                url,
                headers=headers,
                params=params,
                timeout=10
            )

            response.raise_for_status()

            return response

        except requests.exceptions.RequestException as e:
            logger.warning(f"Request failed (Attempt {attempt}): {e}")

            if attempt == max_retries:
                logger.error(f"All {max_retries} attempts failed for {url}")
                return None

            logger.info(f"Retrying in {delay} seconds...")
            time.sleep(delay)
            delay *= 2  
