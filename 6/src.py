f = open("test.txt", "r")

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
        currentGroupList = currentGroupList.union(newLineGroup)

currentTotal = currentTotal + len(currentGroupList) - 1
print("currentTotal: " + str(currentTotal))




