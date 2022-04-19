# canSum
# arguments: targetSum, array of numbers (non negative)

# return boolean indicating if the sum it is possible using the numbers in array
# use an element of the array as many times as needed

# ex.1: can_sum(7, [5, 3, 4, 7]) -> True
# ex.2: can_sum(7, [2, 4]) -> False


def can_sum(target, arr):
    # m: target sum , n: array length
    # time O(n^m)
    # space O(m)

    if target == 0:
        return True

    if target < 0:
        return False

    for n in range(len(arr)):
        new_target = target - arr[n]

        if can_sum(new_target, arr):
            return True

    return False


def can_sum_memo(target, arr, memo={}):
    # m: target sum , n: array length
    # time O(m*n)
    # space O(m)

    if target in memo.keys():
        return memo[target]

    if target == 0:
        return True

    if target < 0:
        return False

    for n in range(len(arr)):
        new_target = target - arr[n]

        if can_sum_memo(new_target, arr):
            memo[target] = True
            return True

    memo[target] = False
    return False


def can_sum_tab(target, arr):
    # m: target sum , n: array length
    # time O(n*n)
    # space O(m)

    # boolean array length target+1
    table = [False for i in range(target + 1)]

    # index 0 -> table[0] = True
    table[0] = True

    # strategy:
    # "add" table[i] to table withs index in arr
    # table[i] -> table[arr[n] +i]

    for i in range(target + 1):

        for n in range(len(arr)):

            if arr[n] + i <= target:
                if table[i]:
                    table[arr[n] + i] = table[i]

    return table[target]


if __name__ == '__main__':
    # print(can_sum(7, [2, 3]))
    # print(can_sum_memo(7, [2, 3]))
    print(can_sum_tab(7, [2, 3]))
    # True

    # print(can_sum(7, [5, 3, 4, 7]))
    # print(can_sum_memo(7, [5, 3, 4, 7]))
    print(can_sum_tab(7, [5, 3, 4, 7]))
    # True

    # print(can_sum(7, [2, 4]))
    # print(can_sum_memo(7, [2, 4]))
    print(can_sum_tab(7, [2, 4]))
    # False

    # print(can_sum(8, [2, 3, 5]))
    # print(can_sum_memo(8, [2, 3, 5]))
    print(can_sum_tab(8, [2, 3, 5]))
    # True

    # print(can_sum(300, [7, 14]))
    # print(can_sum_memo(300, [7, 14]))
    print(can_sum_tab(300, [7, 14]))
    # False
