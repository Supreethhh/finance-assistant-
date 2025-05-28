# Scrape earnings data using newspaper3k or BeautifulSoup
from bs4 import BeautifulSoup
import requests

def scrape_earnings_news():
    url = "https://www.reuters.com/markets/companies/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    headlines = []
    for tag in soup.find_all("a"):
        text = tag.get_text().strip()
        if any(keyword in text.lower() for keyword in ["earnings", "profit", "misses", "beats"]):
            headlines.append(text)

    return headlines[:5] if headlines else ["No recent earnings news found."]
