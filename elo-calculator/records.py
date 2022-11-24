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
    randomness (contribute 30%):
        1-5, voted, higher => more random => worth less pts
        Example:
            1 means no luck e.g. Chess
            2 means no luck after set up e.g. Hey that's my fish
            3 means once a turn e.g. Caesar
            4 means multiple times a turn
            5 means luck fest e.g. Monopoly
    length (contribute 30%):
        5-minute step, cap at 120 minutes, longer => worth more pts
"""
game_characteristic = {
    "Critters at War": [1.69, 4, 15],
    "Caesar!": [1.89, 3, 20],
    "Fish": [1.45, 2, 10],
    "Jekyll vs Hyde": [1.85, 3, 15],
    "The Fox in the Forest": [1.57, 3, 25],
    "The Quest for El Dorado": [1.93, 3, 60],
    "Illusion": [1.07, 4, 15],
    "Barenpark": [1.65, 1, 30],
    "Chess": [3.68, 1, 60],
    "TFA": [2.92, 4, 60],
    "Spirit Island": [4.06, 2, 120],
    "Maximum Point": [5, 1, 120],
    "Minimum Point": [1, 5, 5],
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
