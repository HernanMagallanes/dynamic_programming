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


def count_construct_memo(target, word_bank, memo={}):
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
            a = count_construct_memo(strip_L, word_bank, memo)
            counter += a

    memo[target] = counter
    return counter


def count_construct_tab(target, word_bank):
    # m: target length , n: word_bank length
    # time O(n*m^2)
    # space O(m)

    # table length n+1
    table = [0 for i in range(len(target) + 1)]

    # index 0 -> table[0] = 1
    table[0] = 1

    # strategy:
    # iterate through table
    # -> index i in table [0, ... ,  target+1]
    # iterate the word_bank

    #  1st comparison table[i] > 1 // is not None

    # table index i, target[i]
    # table pointer i+ len(word) , target[i + len(word)]

    # 2nd comparison word_bank[n] == target strip <- target[i:i + len(word)]
    # table[i + len(word)] += target[i]

    for i in range(len(table)):

        for word in word_bank:

            if len(target[i:i + len(word)]) < len(word):
                continue

            if table[i] > 0:

                if i <= i + len(word):

                    if word == target[i:i + len(word)]:
                        table[i + len(word)] += table[i]

    return table[len(table) - 1]


if __name__ == '__main__':
    # counter for can_construct
    counter = 0

    # string_target = 'abcdef'
    # word_bank = ['ab', 'abc', 'cd', 'def', 'abcd']
    # 1

    string_target = 'purple'
    word_bank = ['purp', 'p', 'ur', 'le', 'purpl']
    # 2

    # string_target = 'skateboard'
    # word_bank = ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']
    # 0

    # string_target = 'enterapotentpot'
    # word_bank = ['a','p','ent','enter','ot','o','t' ]
    # 4

    # string_target = 'eeeeeeeeeeeeeeeeeeeeeeeeeeeeeef'
    # word_bank = ['e', 'ee', 'eeee', 'eeeee', 'eeeeee']
    # 0

    print(count_construct(string_target, word_bank))
    print(count_construct_memo(string_target, word_bank))
    print(count_construct_tab(string_target, word_bank))
