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


def dynamic_fib(n, values=[]):
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
            values[n - 1] = dynamic_fib(n - 1)

        if values[n - 2] == 0:
            values[n - 2] = dynamic_fib(n - 2)

        values[n] = values[n - 1] + values[n - 2]

    return values[n]


if __name__ == '__main__':
    n = 40
    # 102334155

    start = time.time()
    print(fib(n))
    # 45.582 !

    end = time.time()
    t = round(end - start, 3)
    print(f'traditional time: {t}')

    start = time.time()
    print(dynamic_fib(n))

    end = time.time()
    t = round(end - start, 3)
    print(f'dynamic time: {t}')
