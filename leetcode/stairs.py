"""
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

    1, 1, 1, 1
    2, 1, 1
    1, 2, 1
    1, 1, 2
    2, 2
    What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
"""

def climb(numStairs, stepSizes):
    """
    numStair: int of how many total stairs there are
    stepSizes: list of each step size
    """
    valueTable = {}
    for index in range(numStairs+1):
        valueTable[index] = 0

    valueTable[0] = 1
    for index in range(numStairs+1):
        if valueTable[index] != 0:
            for step in stepSizes:
                if index+step <= numStairs:
                    valueTable[index+step] += valueTable[index]
    return valueTable[numStairs]

# 5 ways
print(climb(4, [1,2]))
print(climb(8,[1,2]))
print(climb(6,[1,3]))
print(climb(6,[3,1]))
