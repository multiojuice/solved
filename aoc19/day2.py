st = input()

myinput = st.split(',')

for i in range(0, len(myinput)):
    myinput[i] = int(myinput[i])

error = False
answer = False
for noun in range (0, 100):
    for verb in range(0, 100):
        """
        How naive
        """
        positions = list.copy(myinput)
        positions[2] = verb
        positions[1] = noun
        for i in range(0, len(positions), 4):
            opcode = positions[i]
            if opcode == 99:
                if positions[0] == 19690720:
                    answer = True
                    print(100 * noun + verb)
                    break
            elif opcode == 1:
                arg1 = positions[positions[i+1]]
                arg2 = positions[positions[i+2]]
                positions[positions[i+3]] = arg1 + arg2
            elif opcode == 2:
                arg1 = positions[positions[i + 1]]
                arg2 = positions[positions[i + 2]]
                positions[positions[i + 3]] = arg1 * arg2
            else:
                error = True
                break

        if answer:
            break
    if answer:
        break
