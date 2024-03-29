from datetime import date

initial_ratings = {
    "Michael": 1500,
    "Christian": 1500,
    "Asier": 1500,
    "Trung": 1500,
    "Trevin": 1500,
}
"""
Game Characteristic:
    weight (contribute 40%):
        1-5, based on bgg, higher => more complex => worth more pts
    turn-to-turn randomness (contribute 20%):
        1-5, voted, higher => more random => worth less pts
        Description
            1: no luck e.g. Chess
            2: very little luck, usually only during setup and open information e.g. Hey that's my fish
            3: moderate amount of luck, but skill is still the main deciding factor e.g. Caesar
            4: luck affects the game greatly e.g Critters at War
            5: luck fest, might as well roll a dice to decide the winner e.g. Monopoly
    length (contribute 25%):
        5-minute step, cap at 120 minutes, longer => worth more pts
    initial advantage (contribute 15%): or imbalance
        1-4, votes, higher => players start with more unbalanced state => worth less pts
        Description:
            1: player(s) start with same state e.g. Chess
            2: player(s) start with non-obvious advantage, either hard to quantify or hard to materialize
            3: player(s) start with some advantage e.g. Jekyll vs Hyde, Great Plains
            4: player(s) start with obvious advantage e.g. Santorini
"""
game_characteristic = {
    # Small games
    "Critters at War": [1.76, 4, 15, 2],
    "Critters at War 2": [1.86, 4, 25, 2],  # No BGG weight
    "Critters at War Epic": [1.9, 3.5, 35, 2],  # No BGG weight
    "Critters at War Extreme": [2.2, 3, 25, 2],  # No BGG weight
    "Caesar!": [1.89, 3, 20, 1],
    "Fish": [1.45, 2, 10, 2],
    "Jekyll vs Hyde": [1.85, 3.5, 20, 3],
    "The Fox in the Forest": [1.57, 3.5, 25, 2],
    "Hive": [2.32, 1, 20, 1],
    "Great Plains": [1.67, 2, 15, 2],
    "Illusion": [1.07, 3.5, 10, 3],
    "Metro X": [1.78, 3, 20, 1],
    "Love Letter": [1.12, 4, 20, 2],
    "Silver & Gold": [1.18, 3.5, 20, 2],
    "Santorini": [1.73, 1, 15, 3],
    "Santorini 3p": [1.73, 1, 15, 4],
    "Arboretum": [2.15, 4.5, 60, 3],
    "Poker": [2.42, 5, 20, 4.5],
    # Medium game
    "Blue Lagoon": [2.02, 2, 50, 1],
    "Parks": [2.15, 3, 50, 2],
    "Targi": [2.34, 3, 60, 2],
    "Res Arcana": [2.62, 3, 45, 2],
    "The Isle of Cats": [2.35, 3, 60, 2],
    "Patchwork": [1.61, 1, 45, 2],
    "Cartographers": [1.89, 4, 45, 1],
    "Cascadia": [1.84, 3.5, 50, 1],
    "The Quest for El Dorado": [1.93, 3.5, 60, 3],
    "Barenpark": [1.65, 2, 45, 1],
    "Chess": [3.68, 1, 30, 1],
    "Lost Ruins of Arnak": [2.88, 3, 60, 2],
    # Big game
    "Viscounts of the West Kingdom": [3.44, 3, 90, 2],
    "Terraforming Mars EA": [2.92, 4, 60, 2],
    "Spirit Island": [4.06, 3, 120, 5],
    "A Feast for Odin": [3.85, 2, 120, 2],
    # Misc
    "Maximum Point": [5, 1, 120, 1],
    "Minimum Point": [1, 5, 5, 4],
    "Competition": [5, 1, 120, 1],
    "Ice Skating": [2.5, 3, 30, 2],
}

matches = [
    [["Asier"], ["Trung"], ["The Fox in the Forest", date(2022, 10, 17)]],
    [["Michael"], ["Asier"], ["Critters at War", date(2022, 10, 17)]],
    [["Trung"], ["Michael"], ["Critters at War", date(2022, 10, 17)]],
    [["Michael"], ["Asier"], ["Critters at War", date(2022, 10, 24)]],
    [["Asier"], ["Michael"], ["Critters at War", date(2022, 11, 1)]],
    [["Trung"], ["Michael"], ["Caesar!", date(2022, 11, 1)]],
    [["Asier"], ["Trung"], ["The Fox in the Forest", date(2022, 11, 2)]],
    [["Michael"], ["Asier"], ["Critters at War", date(2022, 11, 4)]],
    [["Trung"], ["Asier"], ["Jekyll vs Hyde", date(2022, 11, 4)]],
    [["Asier"], ["Trung"], ["Jekyll vs Hyde", date(2022, 11, 4)]],
    [["Trung"], ["Michael"], ["Caesar!", date(2022, 11, 7)]],
    [["Trung"], ["Michael"], ["Critters at War", date(2022, 11, 7)]],
    [["Trung"], ["Michael"], ["Caesar!", date(2022, 11, 8)]],
    [["Asier"], ["Michael"], ["Critters at War", date(2022, 11, 11)]],
    [["Asier"], ["Michael"], ["Caesar!", date(2022, 11, 11)]],
    [["Asier"], ["Michael"], ["Caesar!", date(2022, 11, 11)]],
    [["Michael"], ["Asier"], ["Critters at War", date(2022, 11, 16)]],
    [["Trung"], ["Michael"], ["Caesar!", date(2022, 11, 16)]],
    [["Trung"], ["Christian"], ["Caesar!", date(2022, 11, 16)]],
    [["Michael"], ["Trung"], ["Critters at War", date(2022, 11, 16)]],
    [["Trung"], ["Christian"], ["Caesar!", date(2022, 11, 18)]],
    [["Trung"], ["Christian"], ["Caesar!", date(2022, 11, 18)]],
    [["Michael"], ["Asier"], ["Critters at War", date(2022, 11, 22)]],
    [["Trevin"], ["Trung"], ["Hive", date(2022, 12, 9)]],
    [["Trung"], ["Trevin"], ["Hive", date(2022, 12, 9)]],
    [["Trung"], ["Trevin"], ["Hive", date(2022, 12, 9)]],
    [["Trung"], ["Trevin"], ["Hive", date(2022, 12, 9)]],
    [["Trung"], ["Trevin"], ["Hive", date(2022, 12, 9)]],
    [["Michael"], ["Trung"], ["Critters at War", date(2022, 12, 12)]],
    [["Trung"], ["Trevin"], ["Hive", date(2022, 12, 13)]],
    [["Trung"], ["Trevin"], ["Hive", date(2022, 12, 13)]],
    [["Trevin"], ["Trung"], ["Illusion", date(2022, 12, 13)]],
    [["Trevin"], ["Trung"], ["Michael"], ["Illusion", date(2022, 12, 14)]],
    [["Trung"], ["Asier"], ["Critters at War 2", date(2022, 12, 15)]],
    [["Christian"], ["Trung"], ["Ice Skating", date(2022, 12, 15)]],
    [["Trung"], ["Asier"], ["The Fox in the Forest", date(2022, 12, 16)]],
    [["Christian"], ["Asier"], ["Hive", date(2022, 12, 20)]],
    [["Asier"], ["Christian"], ["Great Plains", date(2022, 12, 20)]],
    [["Trung"], ["Christian"], ["Cartographers", date(2022, 12, 23)]],
    [["Trung"], ["Trevin"], ["Hive", date(2023, 1, 3)]],
    [["Trevin"], ["Asier"], ["Hive", date(2023, 1, 4)]],
    [["Trung"], ["Asier"], ["Critters at War Extreme", date(2023, 1, 5)]],
    [["Asier"], ["Trung"], ["The Fox in the Forest", date(2023, 1, 5)]],
    [["Michael"], ["Asier"], ["Hive", date(2023, 1, 9)]],
    [["Michael"], ["Trung"], ["Critters at War", date(2023, 1, 10)]],
    [["Michael"], ["Trevin"], ["Hive", date(2023, 1, 11)]],  # Michael is first player
    [["Trevin"], ["Michael"], ["Hive", date(2023, 1, 12)]],  # Trevin is first player
    [["Michael"], ["Trevin"], ["Hive", date(2023, 1, 12)]],  # Michael is first player
    [["Trevin"], ["Michael"], ["Hive", date(2023, 1, 12)]],  # Trevin is first player
    [["Trevin"], ["Michael"], ["Hive", date(2023, 1, 12)]],  # Michael is first player
    [["Michael"], ["Trevin"], ["Hive", date(2023, 1, 13)]],  # Michael is first player
    [["Trevin"], ["Michael"], ["Hive", date(2023, 1, 13)]],  # Trevin is first player
    [["Trevin"], ["Michael"], ["Hive", date(2023, 1, 13)]],  # Trevin is first player
    [["Trung"], ["Asier"], ["Cartographers", date(2023, 1, 19)]],
    [
        ["Michael"],
        ["Christian"],
        ["Hive", date(2023, 1, 20)],
    ],  # Michael is first player
    [["Trung"], ["Trevin"], ["Hive", date(2023, 1, 20)]],  # Trevin is first player
    [["Michael"], ["Trevin"], ["Chess", date(2023, 1, 20)]],
    [["Christian"], ["Trung"], ["Asier"], ["Cartographers", date(2023, 1, 20)]],
    [["Christian"], ["Michael"], ["Critters at War", date(2023, 1, 25)]],
    [["Trung"], ["Christian"], ["Asier"], ["Cartographers", date(2023, 1, 26)]],
    [["Asier"], ["Trung"], ["Critters at War 2", date(2023, 1, 30)]],
    [["Asier"], ["Michael"], ["Cascadia", date(2023, 2, 1)]],
    [["Michael"], ["Christian"], ["Asier"], ["Trevin"], ["Cascadia", date(2023, 2, 3)]],
    [["Trevin"], ["Asier", "Trung"], ["Santorini 3p", date(2023, 2, 8)]],
    [
        ["Michael"],
        ["Trung"],
        ["Asier"],
        ["Trevin"],
        ["The Quest for El Dorado", date(2023, 2, 10)],
    ],
    [["Trung"], ["Asier"], ["Caesar!", date(2023, 2, 15)]],
    [["Asier"], ["Trung"], ["Caesar!", date(2023, 2, 15)]],
    [["Trung"], ["Asier"], ["Fish", date(2023, 2, 17)]],
    [["Trung"], ["Asier"], ["Great Plains", date(2023, 2, 17)]],
    [["Asier"], ["Trung"], ["Caesar!", date(2023, 2, 23)]],
    [["Asier"], ["Trung"], ["Caesar!", date(2023, 2, 24)]],
    [["Trevin"], ["Asier"], ["Caesar!", date(2023, 3, 2)]],
    [["Trevin"], ["Asier"], ["Caesar!", date(2023, 3, 2)]],
    [["Trung"], ["Trevin"], ["Caesar!", date(2023, 3, 2)]],
    [["Trung"], ["Trevin"], ["Caesar!", date(2023, 3, 2)]],
    [["Trevin"], ["Asier"], ["Caesar!", date(2023, 3, 3)]],
    [["Trevin"], ["Asier"], ["Caesar!", date(2023, 3, 3)]],
    [["Trung"], ["Trevin"], ["Caesar!", date(2023, 3, 3)]],
    [["Trung"], ["Asier"], ["Caesar!", date(2023, 3, 3)]],
    [["Asier"], ["Trung"], ["The Fox in the Forest", date(2023, 3, 6)]],
    [["Trung"], ["Asier"], ["Trevin"], ["Arboretum", date(2023, 3, 22)]],
    [["Michael"], ["Asier", "Trung", "Trevin"], ["Illusion", date(2023, 3, 31)]],
    [["Trung"], ["Asier"], ["Santorini", date(2023, 4, 12)]],
    [["Asier"], ["Trung"], ["Santorini", date(2023, 4, 12)]],
    [["Asier"], ["Trung"], ["Santorini", date(2023, 4, 12)]],
    [["Trung"], ["Asier"], ["Santorini", date(2023, 4, 12)]],
    [["Asier"], ["Trung", "Trevin", "Michael"], ["Poker", date(2023, 5, 10)]],
    [["Trung"], ["Asier", "Trevin", "Michael"], ["Poker", date(2023, 5, 11)]],
    [["Michael"], ["Trung", "Trevin"], ["Love Letter", date(2023, 5, 11)]],
    [["Michael"], ["Trung", "Trevin", "Asier"], ["Poker", date(2023, 5, 16)]],
]
