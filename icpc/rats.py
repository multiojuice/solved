def rats():
    n = int(raw_input())
    tab = {}
    for num in range(0, n):
        found = False
        line = raw_input()
        components = line.split(' ')
        iterations = int(components[1])
        total = int(components[2])
        tab[str(total)] = total
        for i in range(0,iterations - 1):
            y = 0
            x = total
            degree = 0
            while True:
                if x == 0:
                    break
                z = int(x % 10)
                x = int(x / 10)
                y = y*(10) + z
                degree += 1
            total += y

            x = total
            arr = [0] * 10
            while True:
                if x == 0:
                    break
                z = int(x % 10)
                x = int(x / 10)
                arr[z] += 1
            total = 0
            degree = 0
            for j in range(9, -1, -1):
                while arr[j] != 0:
                    total += j*(10**degree)
                    degree += 1
                    arr[j] -= 1

            st= str(total)
            if st in tab:
                print num + 1, 'R', i + 2
                found = True
                break
            elif len(st) >= 8 and (st[:4] == '1233' and st[-4:] == '4444') or (st[:4] == '5566' and st[-4:] == '7777'):
                print num + 1, 'C', i + 2
                found = True
                break
            else:
                tab[str(total)] = total

        if not found:
            print num + 1, total


rats()



