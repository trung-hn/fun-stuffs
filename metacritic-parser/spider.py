#%%
import requests
from bs4 import BeautifulSoup

import requests

url = "https://www.example.com"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
}

response = requests.get(url, headers=headers)

# do something with the response
urls = [
    "https://www.metacritic.com/browse/games/release-date/available/ps/userscore",
    # "https://www.metacritic.com/browse/games/release-date/available/ps/userscore?page=1",
    "https://www.metacritic.com/browse/games/release-date/available/ps/metascore",
    # "https://www.metacritic.com/browse/games/release-date/available/ps/metascore?page=1",
]

all_games = set()

for url in urls:
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all game titles on the page
    titles = [title.text.strip() for title in soup.find_all("a", class_="title")]

    all_games.update([title.lower() for title in titles])


with open("skip_list.txt", "r") as f:
    skip_list = {title.lower() for title in f.read().splitlines()}

print(len(all_games))
print(len(skip_list))

for game in all_games:
    if game not in skip_list:
        print(game)

# %%
