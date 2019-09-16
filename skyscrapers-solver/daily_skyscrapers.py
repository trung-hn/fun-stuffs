from copy import deepcopy

# Matrix can be put in the following format.
matrix = [[0, 0, 0, 0, 0, 4, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [5, 8, 0, 7, 0, 0, 1, 0, 4],
          [0, 6, 0, 0, 3, 0, 0, 0, 0],
          [0, 0, 0, 6, 5, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 5, 3, 0, 2],
          [4, 0, 3, 0, 0, 0, 0, 2, 0],
          [0, 1, 0, 0, 0, 2, 0, 8, 0],
          [0, 0, 0, 0, 0, 0, 5, 0, 0],
          ]

top = [4, 4, 1, 2, 3, 4, 2, 3, 4]
bot = [3, 2, 3, 5, 3, 1, 4, 3, 2]
left = [3, 4, 3, 1, 5, 2, 2, 4, 2]
right = [5, 3, 2, 5, 3, 3, 3, 1, 2]

# matrix = [[1, 0, 0, 0, 2, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0, 2],
#           [0, 0, 0, 0, 3, 0, 0, 0],
#           [0, 0, 1, 0, 0, 0, 0, 0],
#           [5, 0, 0, 0, 0, 0, 0, 0],
#           ]
#
# top = [0, 0, 0, 0, 0, 6, 0, 0]
# bot = [4, 4, 3, 4, 4, 0, 0, 0]
# left = [2, 1, 0, 3, 0, 2, 0, 3]
# right = [2, 6, 2, 2, 4, 0, 1, 0]

# Program starts here.
size = len(matrix)


def pre_populate_matrix():
    # pre-pop those cells == 1
    for i, val in enumerate(top):
        if val == 1: matrix[0][i] = size
    for i, val in enumerate(left):
        if val == 1: matrix[i][0] = size
    for i, val in enumerate(bot):
        if val == 1: matrix[-1][i] = size
    for i, val in enumerate(right):
        if val == 1: matrix[i][-1] = size


# populate a pool of values at each cell.
def pre_populate_pool(pools):
    for r in range(size):
        for c in range(size):
            # if there is already a val, pool = set(val)
            if matrix[r][c]:
                pools[r][c] = [matrix[r][c]]
            else:
                pool = list(range(1, size + 1))
                for val in matrix[r]:
                    # remove val on the same row from set
                    if val in pool: pool.remove(val)
                for val in [row[c] for row in matrix]:
                    # remove val in the same col from set
                    if val in pool: pool.remove(val)
                pools[r][c] = pool
          
    for col, val in enumerate(top):
        if not val: continue
        for row in range(val - 1):
            for siz in range(size - val + 2 + row, size + 1):
                if siz in pools[row][col]:
                    pools[row][col].remove(siz)

    for col, val in enumerate(bot):
        if not val: continue
        for row in range(val - 1):
            for siz in range(size - val + 2 + row, size + 1):
                if siz in pools[size - 1 - row][col]:
                    pools[size - 1 - row][col].remove(siz)
    #
    for row, val in enumerate(left):
        if not val: continue
        for col in range(val - 1):
            for siz in range(size - val + 2 + col, size + 1):
                if siz in pools[row][col]:
                    pools[row][col].remove(siz)

    for row, val in enumerate(right):
        if not val: continue
        for col in range(val - 1):
            for siz in range(size - val + 2 + col, size + 1):
                if siz in pools[row][size - 1 - col]:
                    pools[row][size - 1 - col].remove(siz)


# return number of building seen from a direction
def number_of_buildings(i: int, j: int, vert: bool = False, reverse: bool = False) -> int:
    loop_over = reversed(range(size)) if reverse else range(size)
    low, count = 0, 0
    for index in loop_over:
        val = matrix[i][index] if not vert else matrix[index][j]
        if val == 0: break
        if val > low:
            count += 1
            low = val
    return count


def is_valid(i, j):
    val = matrix[i][j]
    # existed in row
    if matrix[i].count(val) == 2:
        return False
    # existed in col
    if [row[j] for row in matrix].count(val) == 2:
        return False

    if j == size - 1:  # only check when row is full
        if i == 2: print(matrix)
        no_buildings_left = number_of_buildings(i, j, False, False)
        if left[i] and no_buildings_left != left[i]: return False

        no_buildings_right = number_of_buildings(i, j, False, True)
        if right[i] and no_buildings_right != right[i]: return False

    if i == size - 1:  # only check when column is full
        no_buildings_top = number_of_buildings(i, j, True, False)
        if top[j] and no_buildings_top != top[j]: return False

        no_buildings_bot = number_of_buildings(i, j, True, True)
        if bot[j] and no_buildings_bot != bot[j]: return False
    return True


def backtrack(r=0, c=0):
    if r == size: return True
    pool = pools[r][c]
    for val in pool:
        matrix[r][c] = val
        if is_valid(r, c):
            rv = backtrack(r, c + 1) if c < size - 1 else backtrack(r + 1, 0)
            if rv: return True
        if len(pool) == 1:
            return
    # backtrack here
    matrix[r][c] = 0


def print_matrix(matrix):
    print("  ", "  ".join(map(str, top)))
    for i, row in enumerate(matrix):
        print(left[i], row, right[i])
    print("  ", "  ".join(map(str, bot)))


# Display original matrix
print("Original matrix: ")
print_matrix(matrix)

# Make pool of values for each cell
pools = deepcopy(matrix)
pre_populate_matrix()
pre_populate_pool(pools)

# Print pool of values
print_matrix(pools)

# Run
backtrack()

# Result
print("Resolved matrix: ")
print_matrix(matrix)
