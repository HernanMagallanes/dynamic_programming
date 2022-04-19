# allConstruct
# arguments: string target, word bank of strings

# return a 2D array containing all of the ways that the target can be constructed
# by concatenating elements of the word bank array.
# (2 dimension array, matrix)

# each element of the 2D array should represent one combination that constructs the target.
# reuse elements of word_bank as many times as needed

# ex.1:  allConstruct('abcdef', ['ab','abc','cd','def','abcd', 'ef', 'c'])
# -> [['ab', 'cd', 'ef'], ['ab','c','def'], ['abc','def'], ['abcd', 'ef']]

# ex.2: allConstruct('', ['cat', 'dog']) -> [[]]
# ex.3: allConstruct('bird', ['cat', 'dog']) -> []


def all_construct_tab(target, word_bank):
    # table length target+1
    table = [[] for _ in range(len(target) + 1)]
    # table[n] show the ways to make target[n]

    # index 0 -> table[0] = [[]]
    table[0] = [[]]

    for i in range(len(table)):
        if i >= 5:
            continue

        for word in word_bank:

            if len(target[i:i + len(word)]) < len(word):
                continue

            if word == target[i:i + len(word)]:
                outer_aux = table[i]

                if isinstance(outer_aux[0], list):

                    if target[i + len(word):]:

                        inner_aux = outer_aux[0].copy()
                        inner_aux.append(word)
                        table[i + len(word)].append(inner_aux)

                    else:
                        aux = table[i].copy()

                        for m in range(len(aux)):
                            aux[m].append(word)

                        table[i + len(word)].append(aux)

    # pass
    return table[len(table) - 1]


if __name__ == '__main__':
    string_target = 'abcdef'
    word_bank = ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']
    # [['ab', 'cd', 'ef'], ['ab','c','def'], ['abc','def'], ['abcd', 'ef']]

    # string_target = 'purple'
    # word_bank = ['purp', 'p', 'ur', 'le', 'purpl']
    # [['purp', 'le'], ['p', 'ur', 'p', 'le',]]

    # string_target = 'skateboard'
    # word_bank = ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']
    # []

    # string_target = 'aaaaaaaaz'
    # word_bank = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa']
    # []

    print(all_construct_tab(string_target, word_bank))
