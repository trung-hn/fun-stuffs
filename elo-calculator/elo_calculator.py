from collections import defaultdict
from typing import List
import matplotlib.pyplot as plt
from records import matches, initial_ratings, game_info
from datetime import date

# Theory: https://towardsdatascience.com/developing-a-generalized-elo-rating-system-for-multiplayer-games-b9b495e87802

DIFF = 800
CHANGE_PER_GAME = 60  # how much does winner get awarded
ALPHA = 1.1  # how much does 1st pos win compared to 2nd and 3rd (only matter in 2+ player games)
OFFSET_PER_GAME = 2


class History:
    def __init__(self, init_ratings) -> None:
        self._ratings = init_ratings
        self.history = defaultdict(list)
        self.update_history()

    def update_history(self):
        for k, v in self._ratings.items():
            self.history[k].append(v)

    @property
    def ratings(self):
        return self._ratings

    @ratings.setter
    def ratings(self, ratings):
        self._ratings = self.reset_ratings(ratings)
        self.update_history()

    def reset_ratings(self, ratings):
        return {k: max(100, v) for k, v in ratings.items()}

    def __repr__(self) -> str:
        return str(self._ratings)


def game_award(game):
    """
    Return the adjusted reward of a game based on its characteristic
    """
    weight, randomness, length = game_info[game]
    z_score = 2 ** weight * 10 + (5 - randomness) * 5 + length / 120 * 30
    return z_score / 100 * CHANGE_PER_GAME


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

    for name in participants:
        ratings[name] += (
            game_award(game)
            * (len(participants) - 1)
            * (player_scores[name] - winning_chance[name])
        ) + OFFSET_PER_GAME
    return ratings


def plot_hist(history):
    _, ax = plt.subplots(figsize=(10, 7))
    total = 0
    for person, scores in history.history.items():
        plt.plot(scores, label=person, marker=".")
        x, y = len(scores) - 1, scores[-1] + 0.2
        ax.annotate(round(scores[-1]), (x, y))
        total += scores[-1]
    plt.legend(loc="upper left")
    plt.ylabel("Rating")
    plt.xlabel("Play")
    plt.title(
        f"Ratings as of {date.today()}. \nExtra Elo Points to the pool: {total % 1500} (Offset/player = {OFFSET_PER_GAME})"
    )
    plt.show()


def main():
    history = History(initial_ratings)
    for *match, (game, *_) in matches:
        history.ratings = calculate_new_ratings(initial_ratings, match, game)
    plot_hist(history)


if __name__ == "__main__":
    main()
