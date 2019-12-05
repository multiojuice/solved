def scanIds(fileName):
  twoLettered = 0
  threeLettered = 0

  with open(fileName) as file:
    # go through each line in the file
    for line in file:
      foundTwo = False
      foundThree = False
      letterDict = {}

      # Go through each char in the lines string
      for char in line:
        if char not in letterDict:
          letterDict[char] = 1
        else:
          letterDict[char] += 1
      
      # go through the values in the dictionary and look
      # for a two and three
      for value in letterDict.values():
        if value == 2 and not foundTwo:
          twoLettered += 1
          foundTwo = True
        if value == 3 and not foundThree:
          threeLettered += 1
          foundThree = True
        if foundTwo and foundThree:
          break
  
  return twoLettered * threeLettered

def findSimilar(fileName):
  stringList = []
  with open(fileName) as file:
    # go through each line in the file
    for line in file:
      stringList.append(line)

  for string1 in stringList:
    for string2 in stringList:
      oneDiff = False
      similar = True
      for index in range(len(string1)):
        if string1[index] != string2[index]:
          if not oneDiff:
            oneDiff = True
          else:
            similar = False
            break
        
      if similar and oneDiff:
        return string1, string2

      

print(scanIds('data/day2.txt'))
print(findSimilar('data/day2.txt'))