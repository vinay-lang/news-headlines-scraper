import requests
from bs4 import BeautifulSoup

url = "https://inshorts.com/en/read"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Inshorts headlines are inside <span itemprop="headline">
headlines = soup.find_all(attrs={"itemprop": "headline"})

with open("headlines.txt", "w", encoding="utf-8") as file:
    for i, h in enumerate(headlines, 1):
        text = h.get_text().strip()
        file.write(f"{i}. {text}\n")

print(f"✅ {len(headlines)} headlines saved to 'headlines.txt'")
