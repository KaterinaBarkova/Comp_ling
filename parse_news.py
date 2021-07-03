from bs4 import BeautifulSoup
import requests
import pandas as pd
from preprocess_news import apply_prep
from classify_news import classify

def parse_news(date="2021-06-24"):
    url = "https://www.huffpost.com/archive/"+date

    headers = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
    }

    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, "html.parser")

    archive = soup.find("div", "archive__entries")
    cards = archive.find_all("div", "card__content")

    headlines = []
    short_descriptions = []
    for card in cards:
        headline = card.find("div", "card__headline").find("a").text
        if headline == None:
            headlines.append("")
        else:
            headlines.append(headline)

        short_description = card.find("div", "card__description").find("a").text
        if short_description == None:
            short_descriptions.append("")
        else:
            short_descriptions.append(short_description)

    df = pd.DataFrame({"headline": headlines, "short_description": short_descriptions})
    return df
