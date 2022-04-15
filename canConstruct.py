# canConstruct
# arguments: string target, word bank of strings

# return boolean indicating if the string it is possible using the words in array

# ex.1: can_construct('abcdef', ['ab','abc','cd','def','abcd']) -> True
# ex.2: can_construct('skateboard', ['bo','rd','ate','t','ska','sk','boar']) -> False
# ex.3: can_construct('', ['a','b','c']) -> True

def can_construct(target, word_bank):
    # m: target length , n: word_bank length
    # time O(n^m *m)
    # space O(m^2)

    if target == '':
        return True

    for i in range(len(word_bank)):

        if target.find(word_bank[i]) == 0:
            new_target = target.strip(word_bank[i])
            a = can_construct(new_target, word_bank)

            if a:
                return True

    return False


def dym_can_construct(target, word_bank, memo={}):
    # m: target length , n: word_bank length
    # time O(n*m^2)
    # space O(m^2)

    if target in memo.keys():
        return memo[target]

    if target == '':
        return True

    for i in range(len(word_bank)):

        if target.find(word_bank[i]) == 0:
            new_target = target.strip(word_bank[i])
            a = dym_can_construct(new_target, word_bank, memo)

            if a:
                memo[target] = True
                return True
    memo[target] = False
    return False


if __name__ == '__main__':
    # print(can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
    # print(dym_can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
    # True

    # print(can_construct('skateboard', ['bo','rd','ate','t','ska','sk','boar']))
    # print(dym_can_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
    # False

    # print(can_construct('enterapotentpot', ['a','p','ent','enter','ot','o','t' ]))
    # print(dym_can_construct('enterapotentpot', ['a','p','ent','enter','ot','o','t' ]))
    # True

    print(can_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eeee', 'eeeee', 'eeeeee']))
    # print(dym_can_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eeee', 'eeeee', 'eeeeee']))
    # False

'''
    ex. 1
    target= 'abcdef'
     word_bank = ['ab','abc','cd','def','abcd'])

abcdef ->

[ab] -> cdef [cd]-> ef False
[abc] -> def [def]-> '' True
[abcd] -> ef False

======================================

    ex. 2
    target= 'skateboard'
     word_bank = ['bo','rd','ate','t','ska','sk','boar'])

skateboard ->

[sk]-> ateboard [ate]-> board [bo]-> ard False
                              [boar]-> d False
[sla]-> teboard [t]-> eboard False

'''
