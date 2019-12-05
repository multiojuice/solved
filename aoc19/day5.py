import math

st = ""
with open("/Users/multiojuice/Projects/solved/aoc19/input5") as file:
    st = file.readline()

myinput = st.split(',')

for i in range(0, len(myinput)):
    myinput[i] = int(myinput[i])

error = False
answer = False
positions = list.copy(myinput)

i = 0

while i < len(positions):
    opcode = positions[i] % 100

    if opcode == 99:
        break
    elif opcode == 3:
        value = int(input())
        positions[positions[i + 1]] = value
        i += 2
    elif opcode == 4:
        print(positions[positions[i + 1]])
        i += 2
    else:
        arg1 = 0
        if (math.floor(positions[i] / 100)) % 10 == 1:
            arg1 = positions[i + 1]
        else:
            arg1 = positions[positions[i + 1]]

        arg2 = 0
        if math.floor((positions[i] / 1000)) % 10 == 1:
            arg2 = positions[i + 2]
        else:
            arg2 = positions[positions[i + 2]]

        if opcode == 2:
            positions[positions[i + 3]] = arg1 * arg2
        elif opcode == 1:
            positions[positions[i + 3]] = arg1 + arg2
        elif opcode == 7:
            if arg1 < arg2:
                positions[positions[i + 3]] = 1
            else:
                positions[positions[i + 3]] = 0
        elif opcode == 8:
            if arg1 == arg2:
                positions[positions[i + 3]] = 1
            else:
                positions[positions[i + 3]] = 0
        i += 4

        if opcode == 5:
            if arg1 != 0:
                i = arg2
            else:
                i -= 1
        if opcode == 6:
            if arg1 == 0:
                i = arg2
            else:
                i -= 1

print(positions)
