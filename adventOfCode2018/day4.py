import re

def partOne(fileName):
  instructions = []
  instructionsDict = {}
  with open(fileName) as file:
    for line in file:
      time = re.sub(r'\W+', '', line[1:17])
      instructions.append(time)
      instructionsDict[time] = line;
  instructions.sort()

  guardDict = {}
  currentGuard = ''
  awake = True
  lastTime = ''
  for instruction in instructions:
    originalString = instructionsDict[instruction]
    type = originalString[19:]
    if type[0] == 'G':
      currentGuard = type.split()[1]
      if currentGuard not in guardDict:
        guardDict[currentGuard] = {}
    if type[0] == 'f':
      lastTime = originalString[12:17]
    if type[0] == 'w':
      hour = lastTime.split(':')[0]
      minute = lastTime.split(':')[1]
      currentMinute = originalString[12:17].split(':')[1]
      for index in range(int(minute), int(currentMinute)):
        if str(index) in guardDict[currentGuard]:
          guardDict[currentGuard][str(index)] += 1
        else:
          guardDict[currentGuard][str(index)] = 1

  highest = 0
  highestId = ''
  highestMinute = ''
  for guardId in guardDict.keys():
    total = 0
    localHigh = 0
    localMinute = ''
    for timeKey in guardDict[guardId].keys():
      total += guardDict[guardId][timeKey]
      if guardDict[guardId][timeKey] > localHigh:
        localHigh = guardDict[guardId][timeKey]
        localMinute = timeKey
    print(total)
    if total > highest:
        highest = total
        highestId = guardId
        highestMinute = localMinute
  print(highest, highestId, highestMinute)

  def partTwo(fileName):
  instructions = []
  instructionsDict = {}
  with open(fileName) as file:
    for line in file:
      time = re.sub(r'\W+', '', line[1:17])
      instructions.append(time)
      instructionsDict[time] = line;
  instructions.sort()

  guardDict = {}
  currentGuard = ''
  awake = True
  lastTime = ''
  for instruction in instructions:
    originalString = instructionsDict[instruction]
    type = originalString[19:]
    if type[0] == 'G':
      currentGuard = type.split()[1]
      if currentGuard not in guardDict:
        guardDict[currentGuard] = {}
    if type[0] == 'f':
      lastTime = originalString[12:17]
    if type[0] == 'w':
      hour = lastTime.split(':')[0]
      minute = lastTime.split(':')[1]
      currentMinute = originalString[12:17].split(':')[1]
      print(currentMinute)
      for index in range(int(minute), int(currentMinute)):
        if str(index) in guardDict[currentGuard]:
          guardDict[currentGuard][str(index)] += 1
        else:
          guardDict[currentGuard][str(index)] = 1

  highest = 0
  highestId = ''
  highestMinute = ''
  for guardId in guardDict.keys():
    for timeKey in guardDict[guardId].keys():
      if guardDict[guardId][timeKey] > highest:
        highest = guardDict[guardId][timeKey]
        highestId = guardId
        highestMinute = timeKey

  print(guardDict)

  print(highest, highestId, highestMinute)

print(partOne('data/day4.txt'))
