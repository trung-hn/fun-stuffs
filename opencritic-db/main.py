# %%
from dataclasses import dataclass
from datetime import datetime
import requests
import json
import time

url = "https://opencritic-api.p.rapidapi.com/game"

headers = {
    "X-RapidAPI-Key": "9fb706059bmsh1fba0cc07e843bfp126b2bjsn2719442bcbb7",
    "X-RapidAPI-Host": "opencritic-api.p.rapidapi.com",
}
to_ignore_files = ["ignored.txt", "tracked.txt", "played.txt"]


def request_and_archive_data():
    """
    Request data from the given url.
    """
    data = []
    skip = 0
    while 1:
        params = {
            # "platforms": "pc",
            "sort": "score",
            "order": "desc",
            "skip": skip,
        }
        res = requests.get(url, headers=headers, params=params)
        time.sleep(0.25)
        print(skip)
        data.extend(res.json())
        if 0 < data[-1]["topCriticScore"] < 75:
            break
        skip += 20
    json.dump(data, open("data.json", "w"))


@dataclass
class GameInfo:
    name: str
    tier: str
    percent_recommended: float
    top_critic_score: float
    game_id: int
    first_release_date: str

    @property
    def release_year(self):
        return datetime.strptime(self.first_release_date, "%Y-%m-%dT%H:%M:%S.%fZ").year


def main(year=2023):
    # request_and_archive_data()

    ignored = set()
    for file in to_ignore_files:
        with open(file, "r") as f:
            ignored |= set(f.read().splitlines())

    with open("data.json", "r") as f:
        data = json.load(f)

    left_overs = []
    for game in data:
        game_info = GameInfo(
            game["name"],
            game["tier"],
            game["percentRecommended"],
            game["topCriticScore"],
            game["id"],
            game["firstReleaseDate"],
        )
        if game_info.release_year != year:
            continue
        # if game_info.tier in ("Mighty",):
        # if game_info.tier in ("Mighty", "Strong"):
        if game_info.top_critic_score > 83:
            if game_info.name in ignored:
                continue
            left_overs.append(game_info.name)
    # left_overs.sort()
    with open("left_overs.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(left_overs))


if __name__ == "__main__":
    main()

# %%
