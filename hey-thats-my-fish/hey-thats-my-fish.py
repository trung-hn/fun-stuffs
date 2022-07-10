# %%
import random
from math import sin, cos, pi, ceil
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon, Circle
from matplotlib.backends.backend_pdf import PdfPages
import argparse

DEFAULT_MAP_SIZE = (10, 10)
MAP_CHOICES = ["RECTANGLE", "TRIANGLE", "DIAMOND"]
FISH_ANGLES = {i: [j / i * 2 * pi for j in range(i)] for i in range(6)}
COLORS = ["white", "green", "purple", "orange", "red", "blue"]
FISH_GROUP_RADIUS = [0, 0.2, 0.2, 0.2, 0.2, 0.2]
FISH_RADIUS = [0, 0.13, 0.12, 0.11, 0.10, 0.09]
FIVE_TILE_CHANCE = 0.05
TILES_PERCENTAGE = [-1, 50, 33, 16, -1, -1]
VERTICLE_SPACING = 0.866667
ZERO_PERCENTAGES = (0, 10)

parser = argparse.ArgumentParser()
parser.add_argument(
    "--rows", type=int, help="Map size in rows", default=DEFAULT_MAP_SIZE[0]
)
parser.add_argument(
    "--cols", type=int, help="Map size in columns", default=DEFAULT_MAP_SIZE[1]
)
parser.add_argument(
    "--shape",
    help="Shape of the map. DEFAULT: RANDOM",
    choices=MAP_CHOICES,
    default="RANDOM",
)
parser.add_argument("--no", help="Number of maps to generate", default=1, type=int)
parser.add_argument("--out", help="Output file name", default="map.pdf")
args = parser.parse_args()


class MapObject:
    def __init__(self, type, size=DEFAULT_MAP_SIZE) -> None:
        self.size = size
        self.type = type
        self._ratio = None
        self._map = None
        if type == "RECTANGLE":
            self._map = self._generate_rect_map()
        elif type == "TRIANGLE":
            self._map = self._generate_tri_map()
        elif type == "DIAMOND":
            self._map = self._generate_diamond_map()

    @property
    def map(self) -> list:
        return self._map

    @property
    def R(self) -> int:
        return self.size[0]

    @property
    def C(self) -> int:
        if self.type == "TRIANGLE":
            return self.R
        elif self.type == "DIAMOND":
            return ceil(self.R * 1.5 - 1)
        return self.size[1]

    @property
    def ratio(self) -> float:
        return self._ratio

    @property
    def total(self) -> float:
        return sum(i * v for i, v in enumerate(self.ratio))

    @property
    def tiles_cnt(self) -> tuple:
        return sum(self._ratio[1:])

    def _generate_rect_map(self) -> None:
        """Generate map."""
        R, C = self.R, self.C
        fishes = self._generate_fishes(R * C)
        return [(r, c, fishes.pop()) for r in range(R) for c in range(C)]

    def _generate_tri_map(self) -> None:
        """Generate map."""
        R, C = self.R, self.C
        fishes = self._generate_fishes(R * (R + 1) // 2)
        rv = []
        for r in range(R):
            for c in range(C):
                fish = fishes.pop() if r <= c * 2 + 1 < R * 2 - r else 0
                rv.append((r, c, fish))
        return rv

    def _generate_diamond_map(self) -> None:
        """Generate map."""
        R, C = self.R, self.C
        fishes = self._generate_fishes(R * R)
        rv = []
        for r in range(R):
            for c in range(C):
                fish = fishes.pop() if r <= c * 2 + 1 < r + R * 2 else 0
                rv.append((r, c, fish))
        return rv

    def _generate_fishes(self, area) -> None:
        """Generate random amount of fish for the map."""
        zeroes = random.randint(*ZERO_PERCENTAGES) * area // 100
        fives = 1 if random.randint(0, 100) <= FIVE_TILE_CHANCE * 100 else 0
        area = area - zeroes - fives
        ones = TILES_PERCENTAGE[1] * area // 100
        twos = TILES_PERCENTAGE[2] * area // 100
        threes = TILES_PERCENTAGE[3] * area // 100
        fours = area - ones - twos - threes
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


def add_fishes(ax, x, y, amt):
    """Add fishes to a tile"""
    for deg in FISH_ANGLES[amt]:
        cx = FISH_GROUP_RADIUS[amt] * cos(deg) + x
        cy = FISH_GROUP_RADIUS[amt] * sin(deg) + y
        ax.add_patch(Circle((cx, cy), FISH_RADIUS[amt], color=COLORS[amt], alpha=0.5))


def add_tile(ax, x, y, amt):
    """Add a hexagon tile to the map"""
    ax.add_patch(
        RegularPolygon(
            (x, y),
            numVertices=6,
            radius=0.55,
            facecolor=COLORS[amt],
            alpha=0.2,
            edgecolor="black" if amt else "none",
            linewidth=0.2,
        )
    )


def generate_map(map_obj: MapObject):
    """Generate a map and save it to a pdf"""
    _, ax = plt.subplots(1)
    ax.set_aspect("equal")
    for row, col, quantity in map_obj.map:
        x = col + 0.5 if row % 2 else col
        y = row * VERTICLE_SPACING
        add_tile(ax, x, y, quantity)
        add_fishes(ax, x, y, quantity)
    plt.xlim([-1, map_obj.C])
    plt.ylim([-1, map_obj.R * VERTICLE_SPACING])
    plt.axis("off")
    return plt


def generate_maps(args):
    """Generate a number of maps and save them to a pdf"""
    print(f"Generating {args.no} {args.shape} maps with size {args.rows}x{args.cols}")
    with PdfPages(f"./{args.out}") as pdf:
        for i in range(1, args.no + 1):
            shape = args.shape
            if shape == "RANDOM":
                shape = random.choice(MAP_CHOICES)
            map_obj = MapObject(shape, (args.rows, args.cols))
            plt = generate_map(map_obj)
            plt.title(
                f"Map {i}. Type: {map_obj.type}. Size: {map_obj.size}. "
                f"Ratio: {map_obj.ratio}. Tiles: {map_obj.tiles_cnt}. Total: {map_obj.total}. \n"
                f"Ref: bit.ly/fish-map-gen",
                fontsize=7,
            )
            pdf.savefig()
            plt.close()
            print(f"Generated {i} map")
    print("Done. File saved to ./" + args.out)


if __name__ == "__main__":
    generate_maps(args)
