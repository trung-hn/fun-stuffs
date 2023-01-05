import random
from collections import defaultdict
from sortedcontainers import SortedList

ROW_LIMIT = 100 * 10 ** 6
PART_LIMIT = 100


def sol1(partitions):
    """
    Time Complexity: O(N^2)
    """
    partitions = sorted(partitions, reverse=True)

    used = set()
    overall = groups = total_used = 0
    while total_used < len(partitions):
        total = 0
        names = []
        for rows, part in partitions:
            if total + rows > ROW_LIMIT:
                continue
            if part in used:
                continue
            used.add(part)
            names.append(part)
            total += rows
        total_used += len(names)
        overall += total
        groups += 1
        # print(f"{total=}, {len(names)=}")
    print(f"{overall=}, {groups=}")


def sol2(partitions):
    """
    Time Complexity: O(NlogN).
    """

    rows_to_parts = defaultdict(list)
    for rows, name in partitions:
        rows_to_parts[rows].append(name)
    sorted_parts = SortedList([rows for rows, _ in partitions])

    groups = 1
    overall = total = 0
    names = []
    while sorted_parts:
        remainder = ROW_LIMIT - total
        idx = min(sorted_parts.bisect_left(remainder), len(sorted_parts) - 1)
        rows = sorted_parts.pop(idx)
        name = rows_to_parts[rows].pop()
        if total + rows > ROW_LIMIT:
            overall += total
            # print(f"{total=}, {len(names)=}")
            groups += 1
            total = 0
            names = []
        total += rows
        names.append(name)
    overall += total
    # print(f"{total=}, {len(names)=}")
    print(f"{overall=}, {groups=}")


if __name__ == "__main__":
    import time

    # when len(partitions) == 30k, both solutions seems to have comparable running time
    partitions = [(random.randint(500, 100000), f"p{i}") for i in range(100000)]
    t0 = time.time()
    sol1(partitions)
    print(time.time() - t0)

    t0 = time.time()
    sol2(partitions)
    print(time.time() - t0)
