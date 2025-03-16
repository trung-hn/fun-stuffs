import json

with open("reviews.json", "r") as file:
    data = json.load(file)

for game, reviews in data.items():
    if any(r["score"] >= "9" for r in reviews) and all(
        r["score"] >= "8" for r in reviews
    ):
        print(game)
