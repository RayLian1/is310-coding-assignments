import cloudscraper
from bs4 import BeautifulSoup
import pandas as pd

scraper = cloudscraper.create_scraper()

url = "https://basketball.fandom.com/wiki/NBA"

response = scraper.get(url)
soup = BeautifulSoup(response.text, "html.parser")

links = soup.find_all("a")

data = []

for link in links[:50]:
    name = link.text.strip()
    href = link.get("href")

    if name and href:
        data.append({"Name": name, "Link": "https://basketball.fandom.com" + href if href.startswith("/") else href})

df = pd.DataFrame(data)
df.to_csv("fandom_data.csv", index=False)

print("Scraping complete!")