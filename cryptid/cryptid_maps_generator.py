#%%
import base64
import json
from selenium import webdriver
from pathlib import Path
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


import time

DRIVER_PATH = "D:\Workspace\sandbox\chromedriver.exe"
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get("https://ospreypublishing.com/playcryptid/")

#%%
def download_map_to_path(driver, path):
    # Save Image
    canvas = driver.find_element(by=By.XPATH, value="//*[@id='mapCanvas']")
    # get the canvas as a PNG base64 string
    canvas_base64 = driver.execute_script(
        "return arguments[0].toDataURL('image/png').substring(21);", canvas
    )
    # decode
    canvas_png = base64.b64decode(canvas_base64)
    Path(path.rsplit("/", 1)[0]).mkdir(parents=True, exist_ok=True)
    with open(path, "wb") as f:
        f.write(canvas_png)


def save_clues_to_path(path, clues):
    Path(path.rsplit("/", 1)[0]).mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        json.dump(clues, f)


def save_text_to_path(path, clue):
    Path(path.rsplit("/", 1)[0]).mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        f.write(clue)


def save_clues_for_each_player(driver, folder, player_no):
    clues = {}
    for player in range(1, player_no + 1):
        driver.find_element(by=By.XPATH, value="//*[@id='clueButton']").click()
        time.sleep(1)
        clue = driver.find_element(by=By.XPATH, value="//*[@id='clueText']")
        clues[f"Player {player}:"] = clue.text

        save_text_to_path(
            folder + f"player {player} clue.txt",
            clue.text,
        )

        driver.find_element(by=By.XPATH, value="//*[@id='clueButton']").click()
        time.sleep(0.6)

    save_clues_to_path(folder + "clues.json", clues)
    return clues


# %%
visited = set()
drop_down = Select(driver.find_element(by=By.XPATH, value="//*[@id='ngfPlayers']"))

for order in range(1, 101):
    for player_no in (2, 3, 4, 5):
        drop_down.select_by_value(str(player_no))
        time.sleep(0.5)
        # Start Game
        driver.find_element(by=By.XPATH, value="//*[@id='ngfStart']").click()
        time.sleep(0.1)
        try:
            driver.find_element(
                by=By.XPATH, value='//button[normalize-space()="OK"]'
            ).click()
        except:
            pass
        time.sleep(0.5)
        folder = f"data/Advance {player_no} players/Game {order}/"
        download_map_to_path(driver, folder + "map.png")

        # Save clues for each player
        clues = save_clues_for_each_player(driver, folder, player_no)
        jsonified_clues = json.dumps(clues)
        if jsonified_clues in visited:
            print(f"{order} already visited")
            continue
        visited.add(jsonified_clues)

        # Get hint
        time.sleep(1)
        driver.find_element(
            by=By.XPATH, value='//button[normalize-space()="Reveal Hint"]'
        ).click()
        time.sleep(0.1)
        driver.find_element(value="hint_confirm_yes").click()
        time.sleep(0.4)
        hint = driver.find_element(by=By.XPATH, value="//*[@id='hintText']")
        save_text_to_path(folder + "hint.txt", hint.text)

        # Get solution
        driver.find_element(value="targetButton").click()
        time.sleep(0.1)
        driver.find_element(value="target_confirm_yes").click()
        time.sleep(1)
        download_map_to_path(driver, folder + "solution/solution.png")

        # Quit
        driver.find_element(by=By.XPATH, value="//*[@id='quitButton']").click()
        time.sleep(0.4)
        try:
            driver.find_element(
                by=By.XPATH, value="//*[@id='quit_confirm_yes']"
            ).click()
        except:
            pass
        time.sleep(0.5)

# %%
