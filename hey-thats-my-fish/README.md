# Hey, That's My Fish Map Generator

Game page: [BGG link](https://boardgamegeek.com/boardgame/8203/hey-s-my-fish)

## Usages

```bash
$ python hey-thats-my-fish.py --help
usage: hey-thats-my-fish.py [-h] [--rows ROWS] [--cols COLS] [--shape {RECTANGLE,TRIANGLE,DIAMOND}] [--no NO]
                            [--out OUT]

optional arguments:
  -h, --help            show this help message and exit
  --rows ROWS           Map size in rows
  --cols COLS           Map size in columns
  --shape {RECTANGLE,TRIANGLE,DIAMOND}
                        Shape of the map. DEFAULT: RANDOM
  --no NO               Number of maps to generate
  --out OUT             Output file name
```

## How to run script

```bash
cd hey-thats-my-fish
pip install -r requirements.txt
python hey-thats-my-fish.py --rows 12 --cols 12 --no 100 --out map.pdf
```

This will generate 100 maps with RANDOM shape (RECTANGLE or TRIANGLE or DIAMOND) with size 12x12 and save them to `map.pdf`.

## Example

![image](https://user-images.githubusercontent.com/39042628/178113474-4c93e9b3-af8c-40a5-8221-04ad34a8dec7.png)

![image](https://user-images.githubusercontent.com/39042628/178113501-42f4aed7-0392-4ff3-8d02-cd3b3e5a9160.png)

![image](https://user-images.githubusercontent.com/39042628/178113517-dba98d4d-03aa-46f9-851e-152116d761db.png)


## Notes

- 1-fish, 2-fish, 3-fish, 4-fish:  tiles ratio: 50%, 33%, 16%, 1%
- ONE 5-fish tile has 5% of appearing
