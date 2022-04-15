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


def dym_can_sum(target, arr, memo={}):
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

        if dym_can_sum(new_target, arr):
            memo[target] = True
            return True

    memo[target] = False
    return False


if __name__ == '__main__':
    # print(can_sum(7, [2, 3]))
    # print(dym_can_sum(7, [2, 3]))
    # True

    # print(can_sum(7, [5, 3, 4, 7]))
    # print(dym_can_sum(7, [5, 3, 4, 7]))
    # True

    # print(can_sum(7, [2, 4]))
    # print(dym_can_sum(7, [2, 4]))
    # False

    # print(can_sum(8, [2, 3, 5]))
    # print(dym_can_sum(8, [2, 3, 5]))
    # True

    # print(can_sum(300, [7, 14]))
    print(dym_can_sum(300, [7, 14]))
    # False

''' 
target [7] array  [5, 3, 4, 7]
Neg value: False

7 -> 
    [5] -> 2 -> F                   
    
    [3] -> 4 -> [4] -> 0 T [3,4]
                [3] -> 1 F
                
    [4] -> 3 -> [3] -> 0 T [4,3]
                
    [7] -> 0 T [7]

=========================================

target [7] array  [2, 4]

7 -> 
    [2] -> 5 -> [2] -> 3 -> [2] -> 1 F 
                [4] -> 1 F
                
    [4] -> 3 -> [2] -> 1 F
                
====================================

target [8] array  [2, 3, 5]

8 ->
    [2] -> 6 -> [2] -> 4 -> [2] -> 2  -> [2] -> 0 T [2,2,2,2]    
                            [3] -> 1 F
                            
                [3] -> 3 -> [2]-> 1 F
                            [3] -> 0 T [2,3,3]
                            
                [5] -> 1 F
    
    [3] -> 5 -> [2] -> 3 -> [2] -> 1 F
                            [3] -> 0 T [3,2,3]
                            
                [3] -> 2 -> [2] -> 0 T [3,3,2]
                [5] -> 0 T [3,5]
                
    [5] -> 3 -> [2] -> 1 F
                [3] -> 0 T [5, 3]        
'''
