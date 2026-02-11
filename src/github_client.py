import logging

from src.config import GITHUB_API_URL, GITHUB_TOKEN, USER_AGENT
from src.utils import request_with_retry

logger = logging.getLogger(__name__)


def fetch_github_repos():
    repos = []
    page = 1
    per_page = 30

    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/vnd.github+json"
    }

    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"

    while True:
        logger.info(f"Fetching GitHub page {page}")

        params = {
            "q": "language:python",
            "sort": "stars",
            "order": "desc",
            "page": page,
            "per_page": per_page
        }

        response = request_with_retry(
            GITHUB_API_URL,
            headers=headers,
            params=params
        )

        if not response:
            logger.error("Stopping GitHub fetch due to repeated failures.")
            break

        data = response.json()
        items = data.get("items", [])

        if not items:
            logger.info("No more repositories found.")
            break

        for repo in items:
            repos.append({
                "name": repo["name"],
                "owner": repo["owner"]["login"],
                "stars": repo["stargazers_count"],
                "url": repo["html_url"]
            })

        page += 1

        if page > 3:
            logger.info("Stopping after 3 pages (safe API usage).")
            break

    logger.info(f"Total GitHub repos collected: {len(repos)}")
    return repos
