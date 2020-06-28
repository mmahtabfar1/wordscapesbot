import itertools
import math
import ast
from datetime import datetime


def nSquaredArray(arr):
    rowLength = math.ceil(math.sqrt(len(arr)))
    justifiedArray = [arr[n:n + rowLength] for n in range(0, len(arr), rowLength)]

    return justifiedArray


while True:
    print()
    unscramble = input(" Please enter the lowercase string you want to un-scramble: ")
    inputLetters = [n.lower() for n in list(unscramble)]
    print("\n", "Given Letters: ", inputLetters, "\n")

    possiblePermutations = []

    permutationStartTime = datetime.now()

    for i in range(2, len(inputLetters) + 1):
        total = 0
        for subset in set(list(itertools.permutations(inputLetters, i))):
            # We're appending the list of i-length tuples from permutations.
            possiblePermutations.append(''.join(subset))
            total += 1
        print(f' {i}-letter permutations: {total}')

    # this was done to get rid of the empty string permutation from being presented as
    # a possible permutation of the letters.
    possiblePermutations.pop(0)

    permutationEndTime = datetime.now()

    print()
    # print(f' Permutation Start Time: {permutationStartTime},')
    # print(f' Permutation End Time: {permutationEndTime},')
    print(f' Permutation Process Runtime: {permutationEndTime - permutationStartTime}\n')

    if len(possiblePermutations) > 10000:
        res = input(f" WARNING: number of permutations exceeds 10000. "
                    " Are you sure you want to see the full list of permutations(Y/N)?")
    else:
        res = input(" Would you like to see the full list of possible permutations(Y/N)? ")
    if res.lower() == 'y':
        gridPermutations = nSquaredArray(possiblePermutations)
        longest = len(max(possiblePermutations, key=len))
        print()
        for line in gridPermutations:
            print(f'\t', end=' ')
            for word in line:
                print(word + ' ' * ((longest - len(word)) + 1), end=' ')
            print()
        else:
            pass

    with open("wordlist.txt", "r") as wordlist:

        f = ast.literal_eval(wordlist.read())
        answerArray = []

        dictionaryCheckStartTime = datetime.now()

        for permutation in possiblePermutations:
            # print(permutation, f[list(permutation)[0]]) Who guards the guards?
            if permutation in f[list(permutation)[0]]:
                answerArray.append(permutation)

        dictionaryCheckEndTime = datetime.now()

        print()
        # print(f' Dictionary Check Start Time: {dictionaryCheckStartTime},')
        # print(f' Dictionary Check End Time: {dictionaryCheckEndTime},')
        print(f' Dictionary Check Runtime: {dictionaryCheckEndTime - dictionaryCheckStartTime}')

    if len(answerArray) == 1:
        condition = "was"
    else:
        condition = "were"
    print(f'\n Out of {len(possiblePermutations)} possible permutations, '
          f'{len(answerArray)} {condition} found in the dictionary.\n')

    # Sorting the array by increasing length as primary key, alpha as secondary key
    answerArray = sorted(answerArray)
    answerArray.sort(key=len)

    gridMatches = nSquaredArray(answerArray)
    longest = len(max(answerArray, key=len))
    print(f' Words Found:\n')
    for line in gridMatches:
        print(f'\t', end=' ')
        for word in line:
            print(word + ' ' * ((longest - len(word)) + 1), end=' ')
        print()

    while True:
        extra = input("\n Would you like to unscramble another word Y/N? ")
        if extra.lower() == "y":
            break
        elif extra.lower() == "n":
            quit()
        else:
            print("Please respond either Y/N: ")
