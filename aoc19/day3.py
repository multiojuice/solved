import math



wire1 = set()
wire2 = set()
steps1 = {}
steps2 = {}

st1 = ""
st2 = ""



with open('input3') as file:
    st1 = file.readline()
    st2 = file.readline()


st1 = st1.split(',')
st2 = st2.split(',')

x = 0
y = 0
step = 0
for component in st1:
    direction = component[0]
    magnitude = int(component[1:])
    for i in range(1, magnitude + 1):
        step += 1
        if direction == 'R':
            x += 1
        if direction == 'L':
            x -= 1
        if direction == 'D':
            y -= 1
        if direction == 'U':
            y += 1

        cur = str(x) + ',' + str(y)
        wire1.add(cur)
        if cur not in steps1:
            steps1[cur] = step


x = 0
y = 0
step = 0
for component in st2:
    direction = component[0]
    magnitude = int(component[1:])
    for i in range(1, magnitude + 1):
        step += 1
        if direction == 'R':
            x += 1
        if direction == 'L':
            x -= 1
        if direction == 'D':
            y -= 1
        if direction == 'U':
            y += 1

        cur = str(x) + ',' + str(y)
        wire2.add(cur)
        if cur not in steps2:
            steps2[cur] = step


intersections = wire1 & wire2

min_dist = 9999999999

for intersect in intersections:
    curr_dist = steps1[intersect] + steps2[intersect]
    if curr_dist < min_dist:
        min_dist = curr_dist
print(min_dist)