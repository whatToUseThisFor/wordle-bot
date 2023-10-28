file = open("possibleWordleWords.txt", "r")
contents = file.readlines()
for i in range(len(contents)):
    contents[i - 1] = contents[i - 1].replace("\n", "")
print(len(contents))
print(contents)

#get data for narrowing words down and put them in variables
requiredLetters = input("What are the required letters? (don't separate them using anything) ")
unavailableLetters = input("What are the unavailable letters? (don't separate them using anything) ")
order = input('What is the order of the word? (ex. if "a" is the first letter an you do not know the other letters, you would type a----) ')
order2 = input("Where do letters NOT go (same as last one, except put five rows, and you put letters that turn yellow instead of green) ")
order3 = input("")
order4 = input("")
order5 = input("")
order6 = input("")

#turn variables into lists to make it easier
orderList = []
orderList2 = []
requiredLetterList = []
unavailableLetterList = []

if len(requiredLetters) > 0:
    for i in range(len(requiredLetters)):
        requiredLetterList.append(requiredLetters[i])
        
if len(unavailableLetters) > 0:    
    for i in range(len(unavailableLetters)):
        unavailableLetterList.append(unavailableLetters[i])
        

for i in range(5):
    orderList.append(order[i])
    
for i in range(5):
    orderList2.append(order2[i])

for i in range(5):
    orderList2.append(order3[i])
    
for i in range(5):
    orderList2.append(order4[i])
    
for i in range(5):
    orderList2.append(order5[i])
    
for i in range(5):
    orderList2.append(order6[i])
    
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
    
for i in contents:
    if i[0] == str(orderList2[0]) and i not in needToDelete:
        needToDelete.append(i)
    if i[1] == str(orderList2[1]) and i not in needToDelete:
        needToDelete.append(i)
    if i[2] == str(orderList2[2]) and i not in needToDelete:
        needToDelete.append(i)
    if i[3] == str(orderList2[3]) and i not in needToDelete:
        needToDelete.append(i)
    if i[4] == str(orderList2[4]) and i not in needToDelete:
        needToDelete.append(i)
    if i[0] == str(orderList2[5]) and i not in needToDelete:
        needToDelete.append(i)
    if i[1] == str(orderList2[6]) and i not in needToDelete:
        needToDelete.append(i)
    if i[2] == str(orderList2[7]) and i not in needToDelete:
        needToDelete.append(i)
    if i[3] == str(orderList2[8]) and i not in needToDelete:
        needToDelete.append(i)
    if i[4] == str(orderList2[9]) and i not in needToDelete:
        needToDelete.append(i)
    if i[0] == str(orderList2[10]) and i not in needToDelete:
        needToDelete.append(i)
    if i[1] == str(orderList2[11]) and i not in needToDelete:
        needToDelete.append(i)
    if i[2] == str(orderList2[12]) and i not in needToDelete:
        needToDelete.append(i)
    if i[3] == str(orderList2[13]) and i not in needToDelete:
        needToDelete.append(i)
    if i[4] == str(orderList2[14]) and i not in needToDelete:
        needToDelete.append(i)
    if i[0] == str(orderList2[15]) and i not in needToDelete:
        needToDelete.append(i)
    if i[1] == str(orderList2[16]) and i not in needToDelete:
        needToDelete.append(i)
    if i[2] == str(orderList2[17]) and i not in needToDelete:
        needToDelete.append(i)
    if i[3] == str(orderList2[18]) and i not in needToDelete:
        needToDelete.append(i)
    if i[4] == str(orderList2[19]) and i not in needToDelete:
        needToDelete.append(i)
    if i[0] == str(orderList2[20]) and i not in needToDelete:
        needToDelete.append(i)
    if i[1] == str(orderList2[21]) and i not in needToDelete:
        needToDelete.append(i)
    if i[2] == str(orderList2[22]) and i not in needToDelete:
        needToDelete.append(i)
    if i[3] == str(orderList2[23]) and i not in needToDelete:
        needToDelete.append(i)
    if i[4] == str(orderList2[24]) and i not in needToDelete:
        needToDelete.append(i)
            
for i in needToDelete:
    contents.remove(i)
#order list into favorites first
favorites = []
scores = {} 
for word in contents:
    score = 0
    if "a" in word:
        score += 979
    if "b" in word:
        score += 281
    if "c" in word:
        score += 477
    if "d" in word:
        score += 393
    if "e" in word:
        score += 1233
    if "f" in word:
        score += 230
    if "g" in word:
        score += 311
    if "h" in word:
        score += 389
    if "i" in word:
        score += 671
    if "j" in word:
        score += 27
    if "k" in word:
        score += 210
    if "l" in word:
        score += 719
    if "m" in word:
        score += 316
    if "n" in word:
        score += 575
    if "o" in word:
        score += 754
    if "p" in word:
        score += 367
    if "q" in word:
        score += 29
    if "r" in word:
        score += 899
    if "s" in word:
        score += 669
    if "t" in word:
        score += 729
    if "u" in word:
        score += 467
    if "v" in word:
        score += 153
    if "w" in word:
        score += 195
    if "x" in word:
        score += 37
    if "y" in word:
        score += 425
    if "z" in word:
        score += 40
    scores[word] = score
    
scores = dict(sorted(scores.items(), key = lambda item: item[1], reverse = True))

favorites = list(scores.keys())

print(len(favorites))
print(favorites)
