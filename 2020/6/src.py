f = open("input.txt", "r")

lines = f.readlines()
currentGroupList = set()
currentTotal = 0
for line in lines:
    if line == "\n":
        #subtract 1 for the new line
        currentTotal = currentTotal + len(currentGroupList) - 1
        currentGroupList = set()

    else:
        newLineGroup = set(line)
        if len(currentGroupList) == 0:
            currentGroupList = newLineGroup
        else:
            #part 1 - union
            #currentGroupList = currentGroupList.union(newLineGroup)
            #part 2 - interesction
            currentGroupList = currentGroupList.intersection(newLineGroup)

        #print(currentGroupList)

currentTotal = currentTotal + len(currentGroupList) - 1
print("currentTotal: " + str(currentTotal))




