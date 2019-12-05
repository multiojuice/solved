st = input()

positions = st.split(',')

for i in range(0, len(positions)):
    positions[i] = int(positions[i])


positions[2] = 2
positions[1] = 12

error = False
for i in range(0, len(positions), 4):
    opcode = positions[i]
    if opcode == 99:
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

print(positions)