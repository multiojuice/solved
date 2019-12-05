import math

def calcFuel(mass):
    fuel = mass / 3
    fuel = math.floor(fuel)
    return fuel - 2


total = 0
with open("input1") as file:
    for line in file:
        current_mass = int(line)
        total += calcFuel(current_mass)

print(total)
