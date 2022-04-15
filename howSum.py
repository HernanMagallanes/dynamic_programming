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


def dym_how_sum(target, arr, l, memo={}):
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
            memo[target] = dym_how_sum(aux, arr, l, memo)
            if dym_how_sum(aux, arr, l, memo):
                # memo[target] = aux
                l.append(arr[n])
                break

    if l:
        memo[target] = l
        return l

    memo[target] = None
    return None


if __name__ == '__main__':
    lst = []

    # print(how_sum(7, [2, 3], lst))
    # print(dym_how_sum(7, [2, 3], lst))
    # [3, 2, 2]

    # print(how_sum(7, [5, 3, 4, 7], lst))
    # print(dym_how_sum(7, [5, 3, 4, 7], lst))
    # [4, 3]

    # print(how_sum(7, [2, 4], lst))
    # print(dym_how_sum(7, [2, 4], lst))
    # None

    # print(how_sum(8, [2, 3, 5], lst))
    # print(dym_how_sum(8, [2, 3, 5], lst))
    # [2, 2, 2, 2]

    # print(how_sum(300, [7, 14], lst))
    # print(dym_how_sum(300, [7, 14], lst))
    # None

    # print(how_sum(100, [7, 25], lst))
    print(dym_how_sum(100, [7, 25], lst))
    # [25, 25, 25, 25]
