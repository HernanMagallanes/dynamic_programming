# bestSum
# arguments: targetSum, array of numbers (non negative)
# return the shortest combination of elements that add up to exactly the target.

# ex.1: best_sum(7, [5, 3, 4, 7]) -> [7]
# ex.2: best_sum(8, [2, 3, 5]) -> [3, 5]

def best_sum(target, arr):
    # m: target sum
    # n: array length

    # time O(n^m *m)
    # space O(m^2)

    if target == 0:
        return []

    if target < 0:
        return None

    short = None

    for n in range(len(arr)):
        new_target = target - arr[n]
        combination = best_sum(new_target, arr)

        if combination is not None:
            combination.append(arr[n])

            if (short is None) or (len(combination) < len(short)):
                short = combination.copy()

    return short


def dym_best_sum(target, arr, memo={}):
    # m: target sum
    # n: array length

    # time O(m^2 *n)
    # space O(m^2)

    if target in memo.keys():
        return memo[target]

    if target == 0:
        return []

    if target < 0:
        return None

    short = None

    for n in arr:
        new_target = target - n
        combination = dym_best_sum(new_target, arr, memo)

        if combination is not None:
            combination.append(n)

            if (short is None) or (len(combination) < len(short)):
                short = combination.copy()

    memo[target] = short
    return short


if __name__ == '__main__':
    # print(best_sum(7, [5, 3, 4, 7]))
    # print(dym_best_sum(7, [5, 3, 4, 7]))
    # [7]

    # print(best_sum(8, [2, 3, 5]))
    # print(dym_best_sum(8, [2, 3, 5]))
    # [3, 5]

    # print(best_sum(8, [5, 4, 1]))
    # print(dym_best_sum(8, [5, 4, 1]))
    # [4, 4]

    # print(best_sum(100, [25, 5, 2, 1]))
    print(dym_best_sum(100, [25, 5, 2, 1]))
    # [25, 25, 25, 25]
