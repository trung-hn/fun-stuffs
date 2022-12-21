#%%
import base64
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time

MIN = 10 ** 8
MAX = 10 ** 9

SAVE_FOLDER = r"D:\Workspace\temp\cartographers-maps"
DRIVER_PATH = "D:\Workspace\sandbox\chromedriver.exe"
MOUNTAIN_RANGE = range(5, 9)
RUINS_DISTRIBUTION = [6, 7, 7, 8, 8, 9]
WASTELAND_DISTRIBUTION = [0, 4, 5] + list(range(6, 12)) * 2 + [12, 13, 14, 15, 16]
print(WASTELAND_DISTRIBUTION)


def setup(identifier):
    prefs = {"download.default_directory": f"{SAVE_FOLDER}\m{identifier}"}
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=options)
    return driver


def download_pdf(driver):
    driver.find_element(by=By.XPATH, value="//*[@id='pdf']").click()
    time.sleep(0.5)


def main():
    for mountains in MOUNTAIN_RANGE:
        driver = setup(mountains)
        for _ in range(40):
            ruins = random.choice(RUINS_DISTRIBUTION)
            wastelands = random.choice(WASTELAND_DISTRIBUTION)
            id = random.randint(MIN, MAX)
            seed = f"{id}.m{mountains}.r{ruins}.w{wastelands}"
            url = f"https://www.cartographers.app/?map={seed}&mountains={mountains}&ruins={ruins}&cliffs={wastelands}"
            print(url)
            driver.get(url)
            download_pdf(driver)
        time.sleep(2)
        driver.quit()


if __name__ == "__main__":
    main()
# %%

# %%
