import math

def calcFuel(mass):
    fuel = mass / 3
    fuel = math.floor(fuel)
    fuel = fuel - 2

    if fuel > 0:
        return fuel
    return 0


total = 0
with open("input1") as file:
    for line in file:
        current_mass = int(line)

        fuel = calcFuel(current_mass)
        total += fuel
        while fuel is not 0:
            fuel = calcFuel(fuel)
            total += fuel

print(total)
