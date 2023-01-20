from collections import defaultdict
from typing import List
import matplotlib.pyplot as plt
from records import matches, initial_ratings, game_characteristic
from datetime import date
from math import sqrt
import plotly.express as px
import plotly.graph_objects as go

# Theory: https://towardsdatascience.com/developing-a-generalized-elo-rating-system-for-multiplayer-games-b9b495e87802

DIFF = 800
CHANGE_PER_GAME = 60  # how much does winner get awarded
ALPHA = 1.1  # how much does 1st pos win compared to 2nd and 3rd (only matter in 2+ player games)
OFFSET_PER_GAME = 2


class History:
    def __init__(self, init_ratings) -> None:
        self._ratings = init_ratings
        self.history_ratings = defaultdict(list)
        self._ratings_by_dates = defaultdict(lambda: defaultdict(int))
        self._unique_dates = set()
        self.update_history()
        self.track_ratings_by_dates(date(2022, 10, 17))

    def update_history(self):
        for p, r in self._ratings.items():
            self.history_ratings[p].append(r)

    def track_ratings_by_dates(self, date):
        for p, r in self._ratings.items():
            self._ratings_by_dates[p][date] = r
        self._unique_dates.add(date)

    @property
    def curr_ratings(self):
        """Track current rating of all players"""
        return self._ratings

    @property
    def players(self):
        return list(self._ratings.keys())

    @property
    def ratings_by_date(self, use_non_linear_time=True):
        dates = sorted(list(self._unique_dates))
        if use_non_linear_time:
            dates = list(map(str, dates))
        return {
            p: (list(self._ratings_by_dates[p].values()), dates) for p in self.players
        }

    @property
    def _average(self):
        return sum(self._ratings.values()) / len(self._ratings)

    @curr_ratings.setter
    def curr_ratings(self, ratings):
        self._ratings = ratings
        self.update_history()

    def __repr__(self) -> str:
        return str(self.curr_ratings)


def z_score(game):
    weight, randomness, length, asymmetry = game_characteristic[game]
    return (
        sqrt(16 - (5 - weight) ** 2) * 10
        + (5 - randomness) * 7.5
        + min(length, 120) / 120 * 30
    )


def game_award(game):
    """
    Return the adjusted reward of a game based on its characteristic
    """
    return z_score(game) / 100 * CHANGE_PER_GAME


games = [(game, z_score(game)) for game in game_characteristic]
games.sort(key=lambda x: -x[1])
for game, score in games:
    print(f"{game:<30} {round(score, 2):>6.2f}")


def winning_probability(ratings: dict, diff: int = DIFF):
    """
    Calculate probablity of winning for each player.

    Parameters
    ----------
    ratings:
        Rating of each player
    diff:
        Player A has 90% chance of winning if R_A = R_B + DIFF.
        In other words, how easy it is for weaker player to breach the gap
    """
    rv = {}
    N = len(ratings)
    for player1, rating1 in ratings.items():
        num = 0
        for player2, rating2 in ratings.items():
            if player1 == player2:
                continue
            num += 1 / (1 + 10 ** ((rating2 - rating1) / diff))
        den = N * (N - 1) / 2
        rv[player1] = num / den
    return rv


def final_score(pos, no_pos=2):
    """
    Calculate final score based on winning position.

    Parameters
    ----------
    pos:
        Final position, 1 is winner, 2 is 2nd winner, ... N is loser
    no_players:
        Number of positions in the game
    alpha:
        How many points 1st winner gets compared to 2nd and 3rd.
        Only matters in games with > 2 final positions
    """
    if no_pos == 1:
        return 1
    num = ALPHA ** (no_pos - pos) - 1
    den = sum(ALPHA ** (no_pos - i) - 1 for i in range(1, no_pos + 1))
    return num / den


def calculate_new_ratings(ratings, match, game):
    """
    Calculate new ratings for each player

    Parameters
    ----------
    all_ratings:
        Rating of all players
    match:
        Match result.
        [[A], [B, C], [D]] means A ranks 1st, B & C both rank 2nd, D ranks last
    """
    participants = [name for names in match for name in names]
    player_ratings = {name: ratings[name] for name in participants}
    winning_chance = winning_probability(player_ratings)

    player_scores = {}
    for pos, names in enumerate(match, 1):
        for name in names:
            player_scores[name] = final_score(pos, len(match)) / len(names)

    new_ratings = dict(ratings)
    for name in participants:
        new_ratings[name] += (
            game_award(game)
            * (len(participants) - 1)
            * (player_scores[name] - winning_chance[name])
        ) + OFFSET_PER_GAME
    return new_ratings


def plot_hist(history: History):
    _, (ax0, ax1) = plt.subplots(2, 1, figsize=(10, 12))
    ax0.set_ylabel("Rating")
    ax0.set_xlabel("Play")
    total = 0
    for person, ratings in history.history_ratings.items():
        ax0.plot(ratings, label=person, marker=".")
        x, y = len(ratings) - 1, ratings[-1] + 0.2
        ax0.annotate(round(ratings[-1]), (x, y))
        total += ratings[-1]

    ax1.set_ylabel("Rating")
    ax1.set_xlabel("Date")
    ax1.tick_params(labelrotation=45)
    for person, (ratings, dates) in history.ratings_by_date.items():
        ax1.plot(dates, ratings, label=person, marker=".")
        x, y = dates[-1], ratings[-1] + 0.2
        ax1.annotate(round(ratings[-1]), (x, y))

    ax0.legend(loc='best')
    ax1.legend(loc='best')
    plt.suptitle(
        f"Ratings as of {date.today()}. \nExtra Elo Points to the pool: {total % 1500} (Offset/player = {OFFSET_PER_GAME})"
    )
    plt.show()


def main():
    history = History(initial_ratings)
    for *match, (game, date) in matches:
        history.curr_ratings = calculate_new_ratings(history.curr_ratings, match, game)
        history.track_ratings_by_dates(date)

    plot_hist(history)


if __name__ == "__main__":
    main()
