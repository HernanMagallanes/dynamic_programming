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


def can_construct_memo(target, word_bank, memo={}):
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
            a = can_construct_memo(new_target, word_bank, memo)

            if a:
                memo[target] = True
                return True
    memo[target] = False
    return False


def can_construct_tab(target, word_bank):
    # m: target length , n: word_bank length
    # time O(n* m^2)
    # space O(m)

    # boolean array length target+1
    table = [False for i in range(len(target) + 1)]
    # table represents if it is possible to create string[a:b]

    # index 0 -> True
    table[0] = True

    # strategy:
    # iterate through table
    # -> index i in boolean table [0, ... ,  target+1]
    # iterate the word_bank

    #  1st comparison table[i] = True

    # table index {i} , {target[i]}
    # table pointer {i + len(word)} , {target[i + len(word)]}

    # 2nd comparison word_bank[n] == target strip <- target[i:i + len(word)]
    # if true -> table[i + len(word)] = True

    for i in range(len(table)):

        for word in word_bank:

            if len(target[i:i + len(word)]) < len(word):
                continue

            if table[i]:

                if i <= i + len(word):

                    if word == target[i:i + len(word)]:
                        table[i + len(word)] = True

    return table[len(table) - 1]


def other_dict(target, arr):
    print(target, arr)
    # same but with dict {'letter':boolean}
    pass


if __name__ == '__main__':
    # string_target = 'abcdef'
    # word_bank = ['ab', 'abc', 'cd', 'def', 'abcd']
    # True

    # string_target = 'skateboard'
    # word_bank = ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']
    # False

    # string_target = 'enterapotentpot'
    # word_bank = ['a','p','ent','enter','ot','o','t' ]
    # True

    string_target = 'eeeeeeeeeeeeeeeeeeeeeeeeeeeeeef'
    word_bank =['e', 'ee', 'eeee', 'eeeee', 'eeeeee']
    # False

    print(can_construct(string_target, word_bank))
    print(can_construct_memo(string_target, word_bank))
    print(can_construct_tab(string_target, word_bank))

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
