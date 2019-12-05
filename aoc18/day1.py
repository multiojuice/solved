def findFrequency(fileName):
  frequency = 0
  with open(fileName) as file:
    for line in file:
      frequency += int(line)
  
  return frequency


def findRepeatedFrequency(fileName):
  frequency = 0
  seenFrequencies = {0: True}
  while True:
    with open(fileName) as file:
      for line in file:
        frequency += int(line)

        if frequency not in seenFrequencies:
          seenFrequencies[frequency] = True
        else:
          return frequency

  return frequency


print(findFrequency('data/day1.txt'))
print(findRepeatedFrequency('data/day1.txt'))

