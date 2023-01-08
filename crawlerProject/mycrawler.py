import requests
from bs4 import BeautifulSoup


response = requests.get(
    "https://stackoverflow.com/questions?tab=active&pagesize=50")
# print(response.status_code)
# print(response.text)
soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

all_a_tags = soup.find_all("a", class_="s-link")
for a_tag in all_a_tags:
    print(a_tag.get_text())

# contents = soup.select(".s-post-summary--content-title")
# for content in contents:
#     print(content.getText())
