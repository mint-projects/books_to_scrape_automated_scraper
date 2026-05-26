# Books Scraper

A small Python scraper that downloads book metadata from https://books.toscrape.com and saves results to `data/latest_books.csv`.

**What it does**
- Crawls the site catalogue pages and visits each book page.
- Extracts `title`, `price`, `rating`, `category` and an `insert_date` timestamp.
- Saves results as CSV at `data/latest_books.csv`.

**Project structure**
- `scraper.py` — main scraper script.
- `requirements.txt` — Python dependencies.
- `data/` — output directory (contains `latest_books.csv`).
- `.github/workflows/actions.yml` — GitHub Actions workflow that runs the scraper on schedule and commits results.

**Requirements**
- Python 3.10+ (tested with 3.10)
- Install dependencies:

```bash
python -m venv .venv
.venv\Scripts\activate    # Windows
pip install -r requirements.txt
```

**Run locally**

```bash
python scraper.py
```

The script writes CSV output to `data/latest_books.csv`. It also prints progress and runtime to the console.

**Workflow / Scheduling**
A GitHub Actions workflow is included at `.github/workflows/actions.yml` that installs dependencies, runs `scraper.py`, and commits `data/latest_books.csv` back to the repository on a schedule and on pushes.

**Notes & customization**
- Change the number of pages scraped by editing the loop in `scraper.py` (`for i in range(1, 10):`).
- The script includes a short sleep between requests to avoid overloading the site (`time.sleep(0.2)`).

**License**
This repository has no license file; add one if you want to allow reuse.
