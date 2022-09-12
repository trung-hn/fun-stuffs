# %%
from bs4 import BeautifulSoup
import requests
import unicodedata
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

URL = "https://boardgamegeek.com/collection/user/supermanvungtau?sort=numplays&sortdir=desc&rankobjecttype=subtype&rankobjectid=1&columns=title%7Cthumbnail%7Cstatus%7Crank%7Crating%7Cbggrating%7Cavgrating%7Cnumvoters%7Cplays&geekranks=Board%20Game%20Rank&played=1&objecttype=thing&ff=1&subtype=boardgame"
# %%
def get_plays_using_driver(url):
    plays = []
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)
    for e in driver.find_elements_by_class_name("collection_plays"):
        txt = e.text
        if txt.startswith("Plays"):
            plays.append(int(txt.split(" ")[1]))
    return plays


def get_plays_using_bs4(url):
    plays = []
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    elements = soup.find_all(class_="collection_plays")
    for element in elements:
        txt = unicodedata.normalize("NFKD", element.text).strip()
        if txt.startswith("Plays"):
            plays.append(int(txt.split(" ")[1]))
    return plays


def h_index(plays):
    plays.sort(reverse=True)
    for i, p in enumerate(plays):
        if p < i + 1:
            return i
    return len(plays)


def g_index(plays):
    plays.sort(reverse=True)
    total = 0
    for i, p in enumerate(plays):
        total += p
        if total < (i + 1) ** 2:
            return i
    return len(plays)


def e_index(plays):
    hi = h_index(plays)
    total = sum(plays[:hi])
    e_square = total - hi ** 2
    return e_square ** 0.5


def i10_index(plays):
    return sum(play >= 10 for play in plays)


counters = get_plays_using_bs4(URL)
hi = h_index(counters)
ei = e_index(counters)
gi = g_index(counters)
i10 = i10_index(counters)

with open("plays.txt", "w") as f:
    to_write = [
        f"h-index = {hi}. e-index = {ei}.",
        f"g-index = {gi}",
        f"i10-index = {i10}",
        f"avg index = {(hi + gi + i10)/3}"
    ]
    f.write("\n".join(to_write))

print(f"h-index = {hi}. e-index = {ei}.")
print(f"g-index = {gi}")
print(f"i10-index = {i10}")
print(f"avg index = {(hi + gi + i10)/3}")

# %%
