import requests
from bs4 import BeautifulSoup


def crawl():
    response = requests.get(
        "https://stackoverflow.com/questions?tab=active&pagesize=50")
    soup = BeautifulSoup(response.text, "html.parser")
    contents = soup.select(".s-post-summary--content-title")
    for content in contents:
        print(content.getText().replace('\n', ''))

# todo

# https://realpython.com/introduction-to-python-generators/
