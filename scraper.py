# scraper.py
import requests
from bs4 import BeautifulSoup

def scrape_quotes():
    url = "http://quotes.toscrape.com"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, timeout=30 )
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("span", class_="text")
    authors = soup.find_all("small", class_="author")

    results = []
    for quote, author in zip(quotes, authors):
        results.append(f"{quote.text} — {author.text}")

    return results
if __name__ == "__main__":
    print(scrape_quotes())