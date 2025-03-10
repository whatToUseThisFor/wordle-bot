file = open("possibleWordleWords.txt", "r")
contents = file.readlines()
for i in range(len(contents)):
    contents[i - 1] = contents[i - 1].replace("\n", "")
print(len(contents))
print(contents)

def createList(var):
    var = str(var)
    outputList = []
    for i in range(len(var)):
        outputList.append(var[i])
    return outputList

#get data for narrowing words down and put them in variables
requiredLetters = input("What are the required letters? (don't separate them using anything) ")
unavailableLetters = input("What are the unavailable letters? (don't separate them using anything) ")
order = input('What is the order of the word? (ex. if "a" is the first letter an you do not know the other letters, you would type a----) ')
order2 = input("Where do letters NOT go (same as last one, except put five rows, and you put letters that turn yellow instead of green) ")
for i in range(4):
    order2 = f"{order2}{input("")}"

#turn vars into lists for itering
requiredLetterList = createList(requiredLetters)
unavailableLetterList = createList(unavailableLetters)

orderList = createList(order)
orderList2 = createList(order2)

#start narrowing down words
needToDelete = []
for i in contents:
    for o in range(5):
        if i[o] in unavailableLetterList and not i in needToDelete:
            needToDelete.append(i)
            
for i in needToDelete:
    contents.remove(i)
    
needToDelete = []

for i in contents:
    for o in requiredLetterList:
        if not o in i and not i in needToDelete:
            needToDelete.append(i)

for i in needToDelete:
    contents.remove(i)

needToDelete = []

for i in contents:
    if i[0] != orderList[0] and orderList[0] != "-" and i not in needToDelete:
        needToDelete.append(i)
    if i[1] != orderList[1] and orderList[1] != "-" and i not in needToDelete:
        needToDelete.append(i)
    if i[2] != orderList[2] and orderList[2] != "-" and i not in needToDelete:
        needToDelete.append(i)
    if i[3] != orderList[3] and orderList[3] != "-" and i not in needToDelete:
        needToDelete.append(i)
    if i[4] != orderList[4] and orderList[4] != "-" and i not in needToDelete:
        needToDelete.append(i)
    
for i in needToDelete:
    contents.remove(i)
    
needToDelete = []

idx = 0
for i in contents:
    for o in range(5):
        for index in range(5):
            if idx == 25:
                continue
            if i[index] == str(orderList2[idx]) and i not in needToDelete:
                needToDelete.append(i)
            idx += 1
            
for i in needToDelete:
    contents.remove(i)
#order list into favorites first
favorites = []
letterFrequencies = {"a": 979, "b": 281, "c": 477, "d": 393, "e": 1233, "f": 230, "g": 311, "h": 389, "i": 671, "j": 27, "k": 210, "l": 719, "m": 316, "n": 575, "o": 754, "p": 367, "q": 29, "r": 899, "s": 669, "t": 729, "u": 467, "v": 153, "w": 195, "x": 37, "y": 425, "z": 40}
scores = {} 
for word in contents:
    score = 0
    for key, val in letterFrequencies.items():
        if key in word:
            score += val
    scores[word] = score
    
scores = dict(sorted(scores.items(), key = lambda item: item[1], reverse = True))

favorites = list(scores.keys())

print(len(favorites))
print(favorites)