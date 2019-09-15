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

# Program starts here.
size = len(matrix)


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

    if j == size - 1:
        no_buildings = number_of_buildings(i, j, False, False)
        if left[i] and no_buildings != left[i]: return False

        no_buildings = number_of_buildings(i, j, False, True)
        if right[i] and no_buildings != right[i]: return False

    if i == size - 1:
        no_buildings = number_of_buildings(i, j, True, False)
        if top[j] and no_buildings != top[j]: return False

        no_buildings = number_of_buildings(i, j, True, True)
        if bot[j] and no_buildings != bot[j]: return False

    return True


def backtrack(r=0, c=0):
    # default value
    if r == size: return True
    if matrix[r][c]:
        rv = backtrack(r, c + 1) if c < size - 1 else backtrack(r + 1, 0)
        return rv
    for val in range(1, size + 1):
        matrix[r][c] = val
        if is_valid(r, c):
            rv = backtrack(r, c + 1) if c < size - 1 else backtrack(r + 1, 0)
            if rv: return True
    # backtrack here
    matrix[r][c] = 0


def print_matrix():
    print("  ", "  ".join(map(str, top)))
    for i, row in enumerate(matrix):
        print(left[i], row, right[i])
    print("  ", "  ".join(map(str, bot)))


print("Original matrix: ")
print_matrix()
backtrack()
print("Resolved matrix: ")
print_matrix()
