# countConstruct
# arguments: string target, word bank of strings

# return number of ways that the string can constructed by concatenating elements of the word_bank array
# reuse elements of word_bank as many times as needed

# ex.1: count_construct('abcdef', ['ab','abc','cd','def','abcd']) -> 1
# ex.2: count_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']) -> 2


def count_construct(target, word_bank):
    # m: target length , n: word_bank length
    # time O(m* n^m)
    # space O(m^2)

    global counter

    if target == '':
        counter += 1
        return True

    for word in word_bank:

        strip_L = target[len(word):]
        strip_R = target[:len(word)]

        if word == strip_R:
            count_construct(strip_L, word_bank)

    return counter


def dym_count_construct(target, word_bank, memo={}):
    # m: target length , n: word_bank length
    # time O(n* m^2)
    # space O(m^2)

    counter = 0

    if target in memo.keys():
        return memo[target]

    if target == '':
        return 1

    for word in word_bank:

        strip_L = target[len(word):]
        strip_R = target[:len(word)]

        if word == strip_R:
            a = dym_count_construct(strip_L, word_bank, memo)
            counter += a

    # if memo:
    #     print('\nmemo')
    #     for k, v in memo.items():
    #         print(k, v)

    memo[target] = counter
    return counter


if __name__ == '__main__':
    # counter for can_construct
    counter = 0

    # print(count_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
    # print(dym_count_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
    # 1

    # print(count_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
    # print(dym_count_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
    # 2

    # print(count_construct('skateboard', ['bo','rd','ate','t','ska','sk','boar']))
    # print(dym_count_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
    # 0

    # print(count_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
    # print(dym_count_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
    # 4

    # print(count_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eeee', 'eeeee', 'eeeeee']))
    print(dym_count_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eeee', 'eeeee', 'eeeeee']))
    # 0

'''
    ex. 2
    target= 'purple'
    word_bank = ['purp','p','ur','le','purpl'])

purple

[purp]-> le [le] -> '' 1

[p]-> urple [ur]-> ple [p]-> le [le]-> '' 1

[purpl]-> e 0

 ====== ====== ====== ====== ====== ====== 
 
    target= 'enterapotentpot'
    ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']
 
enterapotentpot
                     
[enter]-> apotentpot [a]-> potentpot [p]-> otentpot 

[ot]-> entpot [ent]-> pot [p]-> ot [ot]-> '' 1
                                   [o]-> t [t]-> '' 1

[o]-> tentpot [t]-> entpot [ent]-> pot [p]-> ot [ot]-> '' 1
                                                [o]-> t [t]-> '' 1
'''
