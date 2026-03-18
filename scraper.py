import requests
import time
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
import os


rate_mapping = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
rows = []
start_time = time.time()
path_to_save_data = (
    os.path.dirname(os.path.abspath(__file__)) + f"/data/latest_books.csv"
)
print(path_to_save_data)


for i in range(1, 5):
    url = f"https://books.toscrape.com/catalogue/page-{i}.html"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error requesting page number: {i} ({e})")
        continue

    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("h3")
    for book in books:
        try:
            book_url = book.find("a")["href"]
            book_response = requests.get(
                "https://books.toscrape.com/catalogue/" + book_url
            )
            book_soup = BeautifulSoup(book_response.text, "html.parser")

            try:
                title = book_soup.find("h1").text
                price = book_soup.find("p", class_="price_color").text[2:]
                rating = rate_mapping[
                    book_soup.find("p", class_="star-rating")["class"][1]
                ]
                category = (
                    book_soup.find("ul", class_="breadcrumb").find_all("a")[-1].text
                )
            except (AttributeError, KeyError) as e:
                print(f"Error parsing the book data: {e}")
                continue

            insert_date = datetime.now()

            row = {
                "title": title,
                "price": price,
                "rating": rating,
                "category": category,
                "insert_date": insert_date,
            }
            print(f"Book {title} scraped!")
            rows.append(row)
            time.sleep(0.2)
        except requests.exceptions.RequestException as e:
            print(f"Error requesting the book page: {e}")
            continue

df = pd.DataFrame(rows)
print(df.head)
print(len(df))

end_time = time.time()

duration_seconds = end_time - start_time

minutes = int(duration_seconds // 60)
seconds = int(duration_seconds % 60)

print(f"Program execution time: {minutes} minutes and {seconds} seconds.")
df.to_csv(path_to_save_data)
