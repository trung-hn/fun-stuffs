from datetime import date

initial_ratings = {
    "Michael": 1500,
    "Christian": 1500,
    "Asier": 1500,
    "Trung": 1500,
    "Trevin": 1500,
}

z_score = {
    "Critters at War": [1.69, 4, 15],  # 50
    "Caesar!": [1.89, 3, 20],  # 70 - 80
    "Fish": [1.45, 2, 10],  #
    "Jekyll vs Hyde": [1.85, 3, 15],  # 65
    "The Fox in the Forest": [1.57, 3, 25],  # 60
    "The Quest for El Dorado": [1.93, 3, 60],  # 60
    "Illusion": [1.07, 5, 15],
    "Barenpark": [1.65, 1, 30],
    "Chess": [3.68, 1, 50],
    "TFA": [2.92, 4, 60],
    "Spirit Island": [4.06, 2, 120],
}

matches = [
    [["Asier"], ["Trung"], [date(2022, 10, 17), "The Fox in the Forest"]],
    # [["Asier"], ["Michael"], [date(2022, 10, 17), "Critters at War", 5]],
    # [["Michael"], ["Asier"], [date(2022, 10, 17), "Critters at War", 5]],
    # [["Michael"], ["Asier"], [date(2022, 10, 17), "Critters at War", 5]],
    [
        ["Michael"],
        ["Asier"],
        [date(2022, 10, 17), "Critters at War"],
    ],  # Full game with the previous 3
    # [["Trung"], ["Michael"], [date(2022, 10, 17), "Critters at War", 5]],
    # [["Trung"], ["Michael"], [date(2022, 10, 17), "Critters at War", 5]],
    # [["Trung"], ["Michael"], [date(2022, 10, 17), "Critters at War", 5]],
    [
        ["Trung"],
        ["Michael"],
        [date(2022, 10, 17), "Critters at War"],
    ],  # Full game with the previous 3
    # [["Trung"], ["Asier"], [date(2022, 10, 17), "The Fox in the Forest", 5]],
    # [["Asier"], ["Trung"], [date(2022, 10, 19), "The Fox in the Forest", 5]],
    # [["Asier"], ["Trung"], [date(2022, 10, 19), "The Fox in the Forest", 5]],
    [
        ["Asier"],
        ["Trung"],
        [date(2022, 11, 2), "The Fox in the Forest"],
    ],  # Full game with the previous 3
    # [["Michael"], ["Asier"],[date(2022, 10, 24), "Critters at War", 5]],
    # [["Michael"], ["Asier"],[date(2022, 10, 24), "Critters at War", 5]],
    [
        ["Michael"],
        ["Asier"],
        [date(2022, 10, 24), "Critters at War"],
    ],  # Full game with the previous 2
    # [["Asier"], ["Michael"], [date(2022, 10, 24), "Critters at War", 5]],
    # [["Asier"], ["Michael"], [date(2022, 11, 1), "Critters at War", 5]],
    [
        ["Asier"],
        ["Michael"],
        [date(2022, 11, 1), "Critters at War"],
    ],  # Full game with the previous 2
    [["Trung"], ["Michael"], [date(2022, 11, 1), "Caesar!"]],
    # [["Michael"], ["Asier"], [date(2022, 11, 4), "Critters at War", 5]],
    [
        ["Michael"],
        ["Asier"],
        [date(2022, 11, 4), "Critters at War"],
    ],  # Full game with the previous 1
    [["Trung"], ["Asier"], [date(2022, 11, 4), "Jekyll vs Hyde"]],  # Full game
    [["Asier"], ["Trung"], [date(2022, 11, 4), "Jekyll vs Hyde"]],  # Full game
    [["Trung"], ["Michael"], [date(2022, 11, 7), "Caesar!"]],
    # [["Trung"], ["Michael"], [date(2022, 11, 7), "Critters at War", 5]],
    # [["Michael"], ["Trung"], [date(2022, 11, 7), "Critters at War", 5]],
    # [["Trung"], ["Michael"], [date(2022, 11, 7), "Critters at War", 5]],
    [
        ["Trung"],
        ["Michael"],
        [date(2022, 11, 7), "Critters at War"],
    ],  # Full game with the previous 3
    [["Trung"], ["Michael"], [date(2022, 11, 8), "Caesar!"]],
    [["Asier"], ["Michael"], [date(2022, 11, 11), "Critters at War"]],
    [["Asier"], ["Michael"], [date(2022, 11, 11), "Caesar!"]],
    [["Asier"], ["Michael"], [date(2022, 11, 11), "Caesar!", 15]],
    [["Michael"], ["Asier"], [date(2022, 11, 16), "Critters at War", 5]],
    [["Trung"], ["Michael"], [date(2022, 11, 16), "Caesar!", 15]],
    [["Trung"], ["Christian"], [date(2022, 11, 16), "Caesar!", 15]],
    [["Michael"], ["Trung"], [date(2022, 11, 16), "Critters at War", 5]],
    [["Trung"], ["Christian"], [date(2022, 11, 18), "Caesar!", 15]],
    [["Trung"], ["Christian"], [date(2022, 11, 18), "Caesar!", 15]],
    [["Michael"], ["Asier"], [date(2022, 11, 22), "Critters at War", 15]],
]
