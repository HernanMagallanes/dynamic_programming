# fibonacci sequence

# memoization concept
# save repeat values, duplicate patterns
# tree graph -> save recursive branches

import time


def fib(n):
    # time O(2^n)
    # space O(n)

    if n <= 2:
        return 1

    return fib(n - 1) + fib(n - 2)


def fib_memo(n, values=[]):
    # time O(n)
    # space O(n)

    while len(values) < n + 1:
        values.append(0)

    # base case
    if n <= 1:
        return n

    # recursive case
    else:
        if values[n - 1] == 0:
            values[n - 1] = fib_memo(n - 1)

        if values[n - 2] == 0:
            values[n - 2] = fib_memo(n - 2)

        values[n] = values[n - 1] + values[n - 2]

    return values[n]


def fib_tab(n):
    # time O(n)
    # space O(n)

    # array length n+1
    array = [0 for i in range(n + 1)]

    # index 1 -> arr[1] =1
    array[1] = 1

    # strategy:
    # add arr[i] to next items
    # arr[i] -> arr[i+1]
    # arr[i] -> arr[i +2]

    for i in range(n):
        array[i + 1] += array[i]

        if i + 2 <= n:
            array[i + 2] += array[i]

    return array[n]


if __name__ == '__main__':
    n = 40
    # 102334155

    '''
    start = time.time()
    print(fib(n))
    end = time.time()

    t = round(end - start, 3)
    print(f'traditional time: {t}')
    '''

    # 45.582 !

    '''     
    start = time.time()
    print(fib_memo(n))
    end = time.time()

    t = round(end - start, 3)
    print(f'memoization time: {t}')
    '''

    print(fib_tab(6))
    # 8
    print(fib_tab(7))
    # 13
    print(fib_tab(8))
    # 21
    print(fib_tab(50))
    # 12586269025
