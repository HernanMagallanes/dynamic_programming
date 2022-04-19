# HowSum
# arguments: targetSum, array of numbers (non negative)

# return any combination of elements that add up to exactly the target.
# if there no combination that adds up to the target, then return None.
# if there are multiple combinations possible, return one.

# ex.1: how_hum(7, [5, 3, 4, 7]) -> [3,4]
# ex.2: how_hum(7, [2, 4]) -> None

def how_sum(target, arr, l):
    # m: target sum, n: array length
    # time O(n^m *m)
    # space O(m)

    if target == 0:
        return True

    if target < 0:
        return False

    for n in range(len(arr)):
        aux = target - arr[n]

        if aux >= 0:
            if how_sum(aux, arr, l):
                l.append(arr[n])
                break

    if l:
        return l
    return None


def how_sum_memo(target, arr, l, memo={}):
    # m: target sum, n: array length
    # time O(n* m^2)
    # space O(m)

    if target in memo.keys():
        return memo[target]

    if target == 0:
        return True

    if target < 0:
        return False

    for n in range(len(arr)):
        aux = target - arr[n]

        if aux >= 0:
            memo[target] = how_sum_memo(aux, arr, l, memo)
            if how_sum_memo(aux, arr, l, memo):
                # memo[target] = aux
                l.append(arr[n])
                break

    if l:
        memo[target] = l
        return l

    memo[target] = None
    return None


def how_sum_tab(target, arr):
    # m: target sum, n: array length
    # time O(n*m^2)
    # space O(m^2)

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
                table[arr[n] + i] = aux

    return table[target]


if __name__ == '__main__':
    lst = []

    # print(how_sum_tab(7, [5, 3, 4]))

    # print(how_sum(7, [2, 3], lst))
    # print(how_sum_memo(7, [2, 3], lst))
    print(how_sum_tab(7, [2, 3]))
    # [3, 2, 2]

    # print(how_sum(7, [5, 3, 4, 7], lst))
    # print(how_sum_memo(7, [5, 3, 4, 7], lst))
    print(how_sum_tab(7, [5, 3, 4, 7]))
    # [4, 3]

    # print(how_sum(7, [2, 4], lst))
    # print(how_sum_memo(7, [2, 4], lst))
    print(how_sum_tab(7, [2, 4]))
    # None

    # print(how_sum(8, [2, 3, 5], lst))
    # print(how_sum_memo(8, [2, 3, 5], lst))
    print(how_sum_tab(8, [2, 3, 5]))
    # [2, 2, 2, 2]

    # print(how_sum(300, [7, 14], lst))
    # print(how_sum_memo(300, [7, 14], lst))
    print(how_sum_tab(300, [7, 14]))
    # None

    # print(how_sum(100, [7, 25], lst))
    # print(how_sum_memo(100, [7, 25], lst))
    print(how_sum_tab(100, [7, 25]))
    # [25, 25, 25, 25]
