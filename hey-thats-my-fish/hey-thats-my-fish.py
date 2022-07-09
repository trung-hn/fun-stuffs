# %%
import random
import sys
from math import sin, cos, pi
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon, Circle
from matplotlib.backends.backend_pdf import PdfPages

DEFAULT_MAP_SIZE = (10, 10)
FISH_ALPHA = 0.5
FISH_ANGLES = {i: [j / i * 2 * pi for j in range(i)] for i in range(2, 6)}
FISH_COLORS = {0: "white", 1: "green", 2: "purple", 3: "orange", 4: "red", 5: "blue"}
FISH_GROUP_RADIUS = 0.2
FISH_RADIUS = {0: 0, 1: 0.13, 2: 0.12, 3: 0.11, 4: 0.10, 5: 0.09}
FIVE_TILE_CHANCE = 0.02
TILES_PERCENTAGE = [-1, 50, 33, 16, -1, -1]
VERTICLE_SPACING = 0.866667
ZERO_PERCENTAGES = (1, 10)


class MapSize:
    def __init__(self, size=DEFAULT_MAP_SIZE) -> None:
        R, C = size
        N = R * C
        self._ratio = None
        pts = self._generate_pts(N)
        self._map = [(r, c, pts.pop()) for r in range(R) for c in range(C)]

    @property
    def map(self) -> list:
        return self._map

    @property
    def ratio(self) -> float:
        return self._ratio

    @property
    def tiles_cnt(self) -> tuple:
        return sum(self._ratio[1:])

    def _generate_pts(self, N) -> None:
        """Generate random amount of fish for the map."""
        zeroes = random.randint(*ZERO_PERCENTAGES) * N // 100
        fives = 1 if random.randint(0, 100) <= FIVE_TILE_CHANCE * 100 else 0
        N = N - zeroes - fives
        ones = TILES_PERCENTAGE[1] * N // 100
        twos = TILES_PERCENTAGE[2] * N // 100
        threes = TILES_PERCENTAGE[3] * N // 100
        fours = N - ones - twos - threes
        pts = (
            [0] * zeroes
            + [1] * ones
            + [2] * twos
            + [3] * threes
            + [4] * fours
            + [5] * fives
        )
        random.shuffle(pts)
        self._ratio = [zeroes, ones, twos, threes, fours, fives]
        return pts


def add_fishes(ax, x, y, amt, color):
    """Add a number of fishes to a tile"""

    if amt == 1:
        ax.add_patch(Circle((x, y), FISH_RADIUS[amt], color=color, alpha=FISH_ALPHA))
    elif amt in FISH_ANGLES:
        for deg in FISH_ANGLES[amt]:
            cx = FISH_GROUP_RADIUS * cos(deg) + x
            cy = FISH_GROUP_RADIUS * sin(deg) + y
            ax.add_patch(
                Circle((cx, cy), FISH_RADIUS[amt], color=color, alpha=FISH_ALPHA)
            )


def add_tile(ax, x, y, value, color):
    """Add a tile to the map"""
    ax.add_patch(
        RegularPolygon(
            (x, y),
            numVertices=6,
            radius=0.56,
            facecolor=color,
            alpha=0.2,
            edgecolor="black" if value else "none",
            linewidth=0.2,
        )
    )


def generate_map(pdf, i, size=DEFAULT_MAP_SIZE):
    """Generate a map and save it to a pdf"""
    _, ax = plt.subplots(1)
    ax.set_aspect("equal")
    map_size = MapSize(size)
    for row, col, value in map_size.map:
        x = col + 0.5 if row % 2 else col
        y = row * VERTICLE_SPACING
        color = FISH_COLORS[value]
        add_tile(ax, x, y, value, color)
        add_fishes(ax, x, y, value, color)
    plt.xlim([-1, size[1]])
    plt.ylim([-1, size[0]])
    plt.axis("off")
    plt.title(
        f"""Map {i}. Size: {size}. Ratio: {map_size.ratio}. Total: {map_size.tiles_cnt}. \nRef: bit.ly/fish-map-gen""",
        fontsize=7,
    )
    plt
    pdf.savefig()
    plt.close()


def generate_maps(amt, size=DEFAULT_MAP_SIZE, file_name="map.pdf"):
    """Generate a number of maps and save them to a pdf"""
    with PdfPages(f"./{file_name}") as pdf:
        for i in range(1, amt + 1):
            generate_map(pdf, i, size)
            print(f"Generated {i} map")


if __name__ == "__main__":
    row = int(sys.argv[1])
    col = int(sys.argv[2])
    file_name = sys.argv[3]
    number_of_maps = int(sys.argv[4])
    print(f"Generating {number_of_maps} maps with size {row}x{col}")
    generate_maps(number_of_maps, (row, col), file_name)
    print("Done. File saved to ./" + file_name)
