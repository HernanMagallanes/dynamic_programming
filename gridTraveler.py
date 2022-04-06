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


def dym_grid_traveler(n, m, table={}):
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
    table[key] = dym_grid_traveler(m - 1, n) + dym_grid_traveler(m, n - 1)
    return table[key]


if __name__ == '__main__':
    # print(grid_traveler(3, 3))
    # print(grid_traveler(9, 9))
    # print(grid_traveler(18, 18))

    print(dym_grid_traveler(3, 3))
    print(dym_grid_traveler(9, 9))
    print(dym_grid_traveler(18, 18))
