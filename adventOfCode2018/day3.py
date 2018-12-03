def partOne(fileName):
  fabricMap = {}
  collisions = 0
  with open(fileName) as file:
    for line in file:
      instructions = line.split(' ')
      distances = instructions[2][:-1].split(',')
      size = instructions[3].strip().split('x')
      for indexX in range(int(size[0])):
        for indexY in range(int(size[1])):
          if (str(int(distances[0]) + indexX) + 'X' + str(int(distances[1]) + indexY)) in fabricMap and (fabricMap[str(int(distances[0]) + indexX) + 'X' + str(int(distances[1]) + indexY)] is not True):
            fabricMap[str(int(distances[0]) + indexX) + 'X' + str(int(distances[1]) + indexY)] = True
            collisions += 1
          elif (str(int(distances[0]) + indexX) + 'X' + str(int(distances[1]) + indexY)) not in fabricMap:
            fabricMap[str(int(distances[0]) + indexX) + 'X' + str(int(distances[1]) + indexY)] = False
  return collisions


def partTwo(fileName):
  fabricMap = {}
  truthMap = {}
  collisions = 0
  with open(fileName) as file:
    for line in file:
      instructions = line.split(' ')
      idNum = instructions[0]
      distances = instructions[2][:-1].split(',')
      size = instructions[3].strip().split('x')
      truthMap[idNum] = True
      for indexX in range(int(size[0])):
        for indexY in range(int(size[1])):
          if (str(int(distances[0]) + indexX) + 'X' + str(int(distances[1]) + indexY)) in fabricMap:
            if (fabricMap[str(int(distances[0]) + indexX) + 'X' + str(int(distances[1]) + indexY)] is not True):
              fabricMap[str(int(distances[0]) + indexX) + 'X' + str(int(distances[1]) + indexY)].append(idNum)
              collisions += 1
            
            for newIdNum in fabricMap[str(int(distances[0]) + indexX) + 'X' + str(int(distances[1]) + indexY)]:
              if newIdNum in truthMap:
                del truthMap[newIdNum]
            
          elif (str(int(distances[0]) + indexX) + 'X' + str(int(distances[1]) + indexY)) not in fabricMap:
            fabricMap[str(int(distances[0]) + indexX) + 'X' + str(int(distances[1]) + indexY)] = [idNum]
  return truthMap.keys()

print(partOne('data/day3.txt'))
print(partTwo('data/day3.txt'))