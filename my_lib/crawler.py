import csv
from typing import Tuple
import requests
from bs4 import BeautifulSoup
from my_lib.conn_post import ConnPost


class CrawlerRuslan:
    BASE_URL = "https://lenta.ru/"

    def __init__(self):
        pass

    def processing(self, link: str) -> Tuple[str, str, str]:
        url = self.BASE_URL + link
        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, "html.parser")
        header = soup.find("span", class_="topic-body__title").text

        text = soup.find_all("p", class_="topic-body__content-text")
        content = "\n".join([line.text for line in text])
        return header, content, url

    def crawling(self):
        resp = requests.get(self.BASE_URL)
        soup = BeautifulSoup(resp.text, "html.parser")
        links = soup.find_all("a", class_="card-mini")

        data = []
        placeholders = []
        for l in links:
            if "https" not in l.get("href"):
                print(l.get("href"))
                header, content, url = self.processing(l.get("href"))
                data.extend([header, content, url])
                placeholders.append("('{}', '{}', '{}')")

        query_insert = (
                "INSERT INTO news (title, content, url) VALUES" + (",".join(placeholders)).format(*data)
        )

        ConnPost().write_db(query_insert)
