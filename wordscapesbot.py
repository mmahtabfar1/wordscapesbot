import itertools


while True:
    print()
    unscramble = input("Please enter the string you want to un-scramble: ")
    inputLetters = list(unscramble)
    print("\n", "Given Letters: ", inputLetters, "\n")

    possibleCombinations = []

    for i in range(0, len(inputLetters) + 1):
        for subset in itertools.permutations(inputLetters,i):
            if subset not in possibleCombinations:
                possibleCombinations.append(subset)

    for i in range(len(possibleCombinations)):
        possibleCombinations[i] = "".join(possibleCombinations[i])
    
    #this was done to get rid of the empty string combination from being presented as
    #a possible combinations of the letters.
    possibleCombinations.pop(0);

    print("possible combinations of the letters", inputLetters, ":", "\n")
    print(possibleCombinations)
    print("\n", "total combinations: ", len(possibleCombinations))

    wordlist = open("wordlist.txt", "r")
    s = "start"

    answerArray = []

    while s != "":
        s = wordlist.readline()
        s = s.strip()
        if s in possibleCombinations and len(s) > 2:
            answerArray.append(s)

    if len(answerArray) == 1:
        condition = "was"
    else:
        condition = "were"

    print("\n", "Out of " + str(len(possibleCombinations)) + " possible combinations " +
    str(len(answerArray) -1) + " " + condition + " found in the dictionary.")
    print("\n", "> ", answerArray)

    wordlist.close()

    while True:
        print("")
        extra = input("Would you like to unscramble another word Y/N? ")
        if extra == "Y" or extra == "y":
            break
        elif extra == "N" or extra == "n":
            quit()
        else:
            print("Please respond either Y/N: ")
