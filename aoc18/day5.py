
def partOne(fileName):
  with open(fileName) as file:
    thinger = ""
    for line in file:
      thinger = line
      touched = False
      firstTime = True
      lastIndex = 1
      while (firstTime or touched):
        firstTime = False
        touched = False
        for index in range(lastIndex,len(thinger)):
          if thinger[index-1] != thinger[index] and thinger[index-1].lower() == thinger[index].lower():
            touched = True
            lastIndex = max(0,index -2)
            if index != len(thinger):
              thinger = thinger[:index-1] + thinger[index+1:]
            else:
              thinger = thinger[:-2]
            break
      return len(thinger)



def helper(line):
  thinger = line
  touched = False
  firstTime = True
  lastIndex = 1
  while (firstTime or touched):
    firstTime = False
    touched = False
    for index in range(lastIndex,len(thinger)):
      if thinger[index-1] != thinger[index] and thinger[index-1].lower() == thinger[index].lower():
        touched = True
        lastIndex = max(0,index - 2)
        if index != len(thinger):
          thinger = thinger[:index-1] + thinger[index+1:]
        else:
          thinger = thinger[:-2]
        break

  return len(thinger)


def partTwo(fileName):
  with open(fileName) as file:
    thinger = ""
    shortest = 456789087
    for line in file:
      thinger = line
      alpha = 'abcdefghijklmnopqrstuvwxyz';
      for char in alpha:
        newThinger = thinger.replace(char, '')
        newThinger = newThinger.replace(char.upper(), '')
        result = helper(newThinger)
        if result < shortest:
          shortest = result

    return shortest


print(partOne('data/day5.txt'))