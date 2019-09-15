
size = 4
matrix = [[0] * size for _ in range(size)]

top = [2, 2, 2, 1]
bot = [2, 1, 3, 4]
left = [3, 3, 1, 2]
right = [1, 2, 3, 3]

def is_valid(i, j):
    val = matrix[i][j]
    # existed in row
    if matrix[i].count(val) == 2:
        return False
    # existed in col
    if [row[j] for row in matrix].count(val) == 2:
        return False
    
    low, count = 0, 0
    for c in range(size):
        if matrix[i][c] > low:
            count += 1
            low = matrix[i][c]
    if count != left[i]: return False

    low, count = 0, 0
    for r in range(size):
        if matrix[r][j] > low:
            count += 1
            low = matrix[i][c]
    if count != top[j]: return False

    low, count = 0, 0
    for c in reversed(range(size)):
        if matrix[i][c] > low:
            count += 1
            low = matrix[i][c]
    if count != right[i]: return False

    low, count = 0, 0
    for r in reversed(range(size)):
        if matrix[r][j] > low:
            count += 1
            low = matrix[i][c]
    if count != top[j]: return False
    return True

def backtrack(r = 0, c = 0):
    print(r, c)
    if r > size: return True
    for val in range(1, size + 1):
        matrix[r][c] = val
        if is_valid(r, c):
            rv = backtrack(r, c + 1) if c < size - 1 else backtrack (r+1, c)
            if rv: return True
    # backtrack here


backtrack()
print(matrix)