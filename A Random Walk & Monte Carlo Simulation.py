# -*- coding: utf-8 -*-
# Fun experiment with random walk

import random
def random_walk(n):
    """Return coordinates after 'n' block random walk."""
    x = y = 0
    for _ in range(n):
        dx, dy = random.choice([(0, 1), (0, -1), (-1, 0), (1, 0)])
        x += dx
        y += dy
    return x, y

number_of_walks = 4000
short_distance = 4
record = []

for i in range(1,40):
    short_walk = 0
    for _ in range(number_of_walks):
        x, y = random_walk(i)
        if abs(x) + abs(y) <= short_distance:
            short_walk += 1
    record.append(short_walk/number_of_walks * 100)
    print("For {}: {:.2f}% are short walk".format(i, short_walk/number_of_walks * 100))


import matplotlib.pyplot as plt

plt.plot(record)
plt.show()