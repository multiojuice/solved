

def howMuch(arr):
    stack = []
    total = 0
    for height in arr:
        if len(stack) < 1:
            stack.append(height)
        elif stack[0] > height:
            stack.append(height)
        elif stack[0] <= height:
            while (len(stack) != 0):
                if (len(stack) >= 2):
                    total += min([height-stack[-1], stack[0]-stack[-1]])
                stack.pop()
            stack.append(height)

    height = stack.pop()
    while (len(stack) != 0):
        if (len(stack) >= 2):
            total += min([height-stack[-1], stack[0]-stack[-1]])
        stack.pop()


    print(total)


howMuch([3,1,2,1,3])

