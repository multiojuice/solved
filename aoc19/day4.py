import math
first = 145852
second = 616942
total = 0

for number in range(first, second + 1):
    previous = number % 10
    number = math.floor(number / 10)
    justRepeated = False
    real_repeat = False
    increasing = True
    repeat = False
    for i in range(0, 5):
        current = number % 10
        if current == previous:
            if justRepeated:
                repeat = False
            else:
                repeat = True
                justRepeated = True
        else:
            justRepeated = False
            if repeat:
                real_repeat = True
        if current > previous:
            increasing = False
            break
        previous = current
        number = math.floor(number / 10)

    if (real_repeat or repeat and justRepeated) and increasing:
        total += 1

print(total)