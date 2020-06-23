import itertools
import math

while True:
    print()
    unscramble = input(" Please enter the string you want to un-scramble: ")
    inputLetters = list(unscramble)
    print("\n", "Given Letters: ", inputLetters, "\n")

    possibleCombinations = []

    for i in range(0, len(inputLetters) + 1):
        for subset in itertools.permutations(inputLetters, i):
            if subset not in possibleCombinations:
                possibleCombinations.append(subset)

    for i in range(len(possibleCombinations)):
        possibleCombinations[i] = "".join(possibleCombinations[i])

    # this was done to get rid of the empty string combination from being presented as
    # a possible combinations of the letters.
    possibleCombinations.pop(0)

    res = input(" Would you like to see the full list of possible combinations(Y/N)? ")
    if res.lower() == 'y':
        print(possibleCombinations)
    else:
        pass

    with open("wordlist.txt", "r") as wordlist:
        s = "start"

        answerArray = []

        while s != "":
            s = wordlist.readline().strip()
            if s in possibleCombinations and len(s) > 2:
                answerArray.append(s)

    if len(answerArray) == 1:
        condition = "was"
    else:
        condition = "were"
    print(f'\n Out of {str(len(possibleCombinations))} possible combinations, '
          f'{str(len(answerArray) - 1)} {condition} found in the dictionary.\n')

    # this sets and makes the grid
    longestWordLength = len(max(answerArray, key=len))
    length = math.ceil(math.sqrt(len(answerArray)))
    justifiedArray = [answerArray[i:i+length] for i in range(0, len(answerArray), length)]

    print(f' Words Found:\n')
    for line in justifiedArray:
        print(f'\t', end=' ')
        for word in line:
            print(word + ' '*((longestWordLength - len(word)) + 1), end=' ')
        print()

    while True:
        extra = input("\n Would you like to unscramble another word Y/N? ")
        if extra.lower() == "y":
            break
        elif extra.lower() == "n":
            quit()
        else:
            print("Please respond either Y/N: ")
