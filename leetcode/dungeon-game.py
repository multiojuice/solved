"""
https://leetcode.com/problems/dungeon-game/description/

The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.
"""


def calculateMinimumHP(dungeon):
    valueArrs = []
    for x in range(len(dungeon)):
        temp = []
        for y in range(len(dungeon[x])):
            # first value is current, next value is min needed health
            temp.append((0,99999))
        valueArrs.append(temp)

    if dungeon[0][0] >= 0:
        valueArrs[0][0] = (dungeon[0][0] + 1, 1)
    else:
        valueArrs[0][0] = ( 1, (-1 * dungeon[0][0]) + 1)

    print(valueArrs)

    for dungeonX in range(dungeon):
        for dungeonY in range(dungeon[0]):
            differenceRight =  min(valueArrs[dungeonX][dungeonY][0] + dungeon[dungeonX + 1][dungeonY], 0) * -1
            differenceDown =  min(valueArrs[dungeonX][dungeonY][0] + dungeon[dungeonX][dungeonY + 1], 0) * -1
            print(difference)
            if valueArrs[dungeonX + 1][dungeonY][1] > valueArrs[dungeonX][dungeonY][0] + difference:
                valueArrs[dungeonX + 1][dungeonY][1] = valueArrs[dungeonX][dungeonY][0] + difference
                if (difference = )
                valueArrs[dungeonX + 1][dungeonY][0] =

            if valueArrs[dungeonX + 1][dungeonY][1] == valueArrs[dungeonX][dungeonY][0] + difference:

calculateMinimumHP([[-4,2,3],[4,5,6]])

