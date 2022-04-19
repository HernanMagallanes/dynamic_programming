# traveler on na 2D grid

# grid nxm (dimensions)
# begin in top-left corner
# travel to bottom-right corner
# only move down or right

# how many ways can you travel ?
# Ex: gridTraveler(2,3) -> 3

# shrinking the effective size of playable area
# (2,3) -> down -> (1,3) -> right -> (1,2) -> right -> (1,1)

# memoization: shrink grids

def grid_traveler(n, m):
    # time O(2^n+m)
    # space O(n+m)

    if m == 1 and n == 1:
        return 1

    if m == 0 or n == 0:
        return 0

    return grid_traveler(m - 1, n) + grid_traveler(m, n - 1)


def grid_traveler_memo(n, m, table={}):
    # m*n possibilities
    # time O(m*n)
    # space O(n+m)

    key = f'{n},{m}'

    if key in table.keys():
        return table[key]

    # base case
    if m == 1 and n == 1:
        return 1

    if m == 0 or n == 0:
        return 0

    # recursive case
    table[key] = grid_traveler_memo(m - 1, n) + grid_traveler_memo(m, n - 1)
    return table[key]


def grid_traveler_tab(n, m):
    # time O(m*n)
    # space O(n*m)

    # grid: matrix (nested lists)
    grid = [[0 for j in range(m + 1)] for i in range(n + 1)]

    # index 1 -> grid[1][1] =1
    grid[1][1] = 1

    # strategy:
    # add grid[i][j] to neighbors
    # grid[i][j] -> grid[i+1][j]
    # grid[i][j] -> grid[i][j+1]

    for i in range(n + 1):
        for j in range(m + 1):
            current = grid[i][j]

            if j + 1 <= m:
                grid[i][j + 1] += current

            if i + 1 <= n:
                grid[i + 1][j] += current

    return grid[n][m]


if __name__ == '__main__':
    # print(grid_traveler(3, 3))
    # print(grid_traveler_memo(3, 3))
    print(grid_traveler_tab(3, 3))
    # 6

    # print(grid_traveler(9, 9))
    # print(grid_traveler_memo(9, 9))
    print(grid_traveler_tab(9, 9))
    # 12870

    # print(grid_traveler(18, 18))
    # print(grid_traveler_memo(18, 18))
    print(grid_traveler_tab(18, 18))
    # 2333606220
