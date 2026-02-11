# Python Data Collector

A production-oriented Python data collection tool that scrapes public website data and consumes the GitHub REST API.

This project demonstrates clean software engineering practices including pagination handling, retry logic with exponential backoff, structured logging, environment-based configuration, and normalized JSON output generation.

---

##  Objective

Build a production-minded Python tool that:

- Scrapes structured data from a public website (HTML parsing)
- Consumes a public API with optional authentication
- Handles pagination for both sources
- Implements retry logic with exponential backoff
- Uses structured logging instead of print statements
- Exports normalized results into a single JSON file
- Handles partial failures gracefully

---

##  Features

- Website scraping using BeautifulSoup
- GitHub REST API consumption
- Pagination handling
- Retry mechanism with exponential backoff
- Structured logging using Python logging module
- Environment variable-based configuration
- Graceful failure handling
- Modular and maintainable architecture

---

##  Tech Stack

- Python 3.12
- requests
- BeautifulSoup4
- python-dotenv
- logging (built-in)

---

## 📁 Project Structure

```
Python_Data_Collector/
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── scraper.py
│   ├── github_client.py
│   ├── utils.py
│   └── config.py
│
├── output/
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

##  Setup & Installation

###  Clone the Repository

```bash
git clone https://github.com/Gopinath-chinnadurai/python-data-collector.git
cd python-data-collector
```

###  Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows**
```bash
venv\Scripts\activate
```

###  Install Dependencies

```bash
pip install -r requirements.txt
```

###  Configure Environment Variables

Create a `.env` file in the root directory:

```
USER_AGENT=MyDataCollector/1.0
OUTPUT_PATH=output/data.json
GITHUB_TOKEN=your_github_token_here
```

> GitHub token is optional but recommended to increase API rate limits.

---

##  Run the Application

From project root:

```bash
python -m src.main
```

---

##  Output

The tool generates:

```
output/data.json
```

### Output Structure

```json
{
  "quotes": [
    {
      "text": "Quote text",
      "author": "Author Name",
      "author_url": "Author profile URL"
    }
  ],
  "github_repos": [
    {
      "name": "repository-name",
      "owner": "owner-name",
      "stars": 12345,
      "url": "repository-url"
    }
  ],
  "meta": {
    "run_time": "ISO-8601 timestamp",
    "total_quotes": 100,
    "total_repos": 90,
    "failures": 0
  }
}
```

---

## Design Decisions

- Modular separation of concerns (scraper, API client, utils, config)
- Centralized retry logic abstraction
- Environment-based configuration (no hardcoded secrets)
- Structured logging for better observability
- Graceful handling of partial failures

---

## ⚠️ Known Limitations

- GitHub pagination limited to first 3 pages to prevent excessive API usage
- Data is exported to JSON instead of a database
- No automated unit tests included

---

##  Production Improvements

If deployed for long-term production usage:

- Add monitoring and alerting
- Detect and handle API rate-limit headers
- Centralized logging system
- Async I/O for performance optimization
- Store results in a database
- Containerize using Docker
- Add unit and integration tests
- Add metrics collection (Prometheus/Grafana)

---

##  Conclusion

This project demonstrates practical Python engineering skills including web scraping, API integration, retry handling, configuration management, structured logging, and normalized data export using a production-minded approach.
