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

#turn variables into lists to make it easier
orderList = []
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
        
print(len(contents))
print(contents)
