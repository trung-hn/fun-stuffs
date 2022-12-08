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
    weight (contribute 35%):
        1-5, based on bgg, higher => more complex => worth more pts
    randomness (contribute 25%):
        1-5, voted, higher => more random => worth less pts
        Description
            1: no luck e.g. Chess
            2: very little luck, usually only during setup e.g. Hey that's my fish
            3: moderate amount of luck, but skill is still the main deciding factor e.g. Caesar
            4: luck affects the game greatly e.g Critters at War
            5: luck fest, might as well roll a dice to decide the winner e.g. Monopoly
    length (contribute 20%):
        5-minute step, cap at 120 minutes, longer => worth more pts
    asymmetry (contribute 20%):
        1-5, votes, higher => players start with more unbalanced state => worth less pts
        This is somewhat related to randomness
        Description:
            1: players start with same state e.g. Chess
            2: players start with small potential imbalance. Games where player order matter e.g. Hey's that my fish
            3: players start with moderate potentital imbalance. Card games like Critters at War, Jekyll vs Hyde
            4: players start with huge potential imbalance e.g. Unmatched
            5: players start with obvious imbalance
"""
game_characteristic = {
    "Critters at War": [1.69, 3, 15, 3],
    "Caesar!": [1.89, 3, 20, 2],
    "Fish": [1.45, 2, 10, 2],
    "Jekyll vs Hyde": [1.85, 3, 15, 3],
    "The Fox in the Forest": [1.57, 3, 25, 3],
    "The Quest for El Dorado": [1.93, 3, 60, 1],
    "Illusion": [1.07, 4, 15, 1],
    "Barenpark": [1.65, 2, 45, 2],
    "Chess": [3.68, 1, 60, 1],
    "TFA": [2.92, 4, 60, 1],
    "Spirit Island": [4.06, 2, 120, 5],
    "Maximum Point": [5, 1, 120, 1],
    "Minimum Point": [1, 5, 5, 5],
}

matches = [
    [["Asier"], ["Trung"], ["The Fox in the Forest", date(2022, 10, 17)]],
    [["Michael"], ["Asier"], ["Critters at War", date(2022, 10, 17)]],
    [["Trung"], ["Michael"], ["Critters at War", date(2022, 10, 17)]],
    [["Asier"], ["Trung"], ["The Fox in the Forest", date(2022, 11, 2)]],
    [["Michael"], ["Asier"], ["Critters at War", date(2022, 10, 24)]],
    [["Asier"], ["Michael"], ["Critters at War", date(2022, 11, 1)]],
    [["Trung"], ["Michael"], ["Caesar!", date(2022, 11, 1)]],
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
]
