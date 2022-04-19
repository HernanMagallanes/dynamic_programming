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


def best_sum_memo(target, arr, memo={}):
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
        combination = best_sum_memo(new_target, arr, memo)

        if combination is not None:
            combination.append(n)

            if (short is None) or (len(combination) < len(short)):
                short = combination.copy()

    memo[target] = short
    return short


def best_sum_tab(target, arr):
    # m: target sum, n: array length
    # time O()
    # space O()

    # table length target+1
    table = [None for i in range(target + 1)]

    # index 0 -> table[0] = []
    table[0] = []

    # strategy:
    # add table[i] to table withs index in arr and arr[n] value

    # if table[i] == [] // i == 0
    #   [] -> table[arr[n] +i] + arr[a]

    # if table[i] is None
    #   continue

    # if len(table[arr[n] + i]) < len(aux):
    #   continue

    # table[i]
    # table[arr[n] +i] append arr[n]

    for i in range(target + 1):

        for n in range(len(arr)):

            if arr[n] + i <= target:

                if i == 0:
                    table[arr[n] + i] = [arr[n]]

                if table[i] is None:
                    continue

                aux = table[i].copy()
                aux.append(arr[n])

                if table[arr[n] + i] is not None:
                    if len(table[arr[n] + i]) < len(aux):
                        continue

                table[arr[n] + i] = aux

    return table[target]


if __name__ == '__main__':
    # print(best_sum(7, [5, 3, 4, 7]))
    # print(best_sum_memo(7, [5, 3, 4, 7]))
    print(best_sum_tab(7, [5, 3, 4, 7]))
    # [7]

    # print(best_sum(8, [2, 3, 5]))
    # print(best_sum_memo(8, [2, 3, 5]))
    print(best_sum_tab(8, [2, 3, 5]))
    # [3, 5]

    # print(best_sum(8, [5, 4, 1]))
    # print(best_sum_memo(8, [5, 4, 1]))
    print(best_sum_tab(8, [5, 4, 1]))
    # [4, 4]

    # print(best_sum(100, [25, 5, 2, 1]))
    # print(best_sum_memo(100, [25, 5, 2, 1]))
    print(best_sum_tab(100, [25, 5, 2, 1]))
    # [25, 25, 25, 25]
