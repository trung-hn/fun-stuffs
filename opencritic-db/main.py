# %%
from dataclasses import dataclass
from re import I
import requests
import json


def request_and_archive_data():
    """
    Request data from the given url.
    """
    data = []
    skip = 0
    while 1:
        res = requests.get(
            f"https://api.opencritic.com/api/game?platforms=pc&sort=score&time=2022&order=desc&skip={skip}"
            ""
        )
        print(skip)
        if res.json():
            data.extend(res.json())
            if 0 < data[-1]["topCriticScore"] < 75:
                break
            skip += 20
        else:
            break
    json.dump(data, open("data.json", "w"))


@dataclass
class GameInfo:
    name: str
    tier: str
    percent_recommended: float
    top_critic_score: float
    game_id: int


def main():
    request_and_archive_data()
    with open("data.json", "r") as f:
        data = json.load(f)

    ignored = set()
    with open("ignored.txt", "r") as f:
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
        )
        if game_info.tier in ("Mighty",):
        # if game_info.tier in ("Mighty", "Strong"):
            if game_info.name in ignored:
                continue
            left_overs.append(game_info.name)
    # left_overs.sort()
    with open("left_overs.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(left_overs))


if __name__ == "__main__":
    main()

# %%
