import sys

def hawaii():
    num_of_tests = int(sys.stdin.readline())

    while(num_of_tests):
        italy = {}
        usa = {}
        num_of_pizzas = int(sys.stdin.readline())
        while(num_of_pizzas):
            name = sys.stdin.readline()
            foreign_ing = sys.stdin.readline().split(' ')[1:]
            foreign_ing[-1] = foreign_ing[-1].strip()
            foreign_ing = set(foreign_ing)

            known_ing = sys.stdin.readline().split(' ')[1:]
            known_ing[-1] = known_ing[-1].strip()
            known_ing = set(known_ing)

            for ing in foreign_ing:
                if ing in italy:
                    italy[ing] = italy[ing].intersection(known_ing)
                else:
                    italy[ing] = known_ing

            for ing in known_ing:
                if ing in usa:
                    usa[ing] = usa[ing].intersection(foreign_ing)
                else:
                    usa[ing] = foreign_ing

            num_of_pizzas -= 1

        temp = {}
        for ing in usa:
            for foreign in usa[ing]:
                if ing in italy[foreign]:
                    if foreign in temp:
                        temp[foreign].add(ing)
                    else:
                        temp[foreign] = {ing}


        for ing in sorted(temp.keys()):
            for known in sorted(temp[ing]):
                print "(" + ing + ", " + known + ")"

        if num_of_tests != 1:
            print ""
        num_of_tests -= 1

hawaii()