

arr = {}

for i in range(1, 10):
    st = ""
    st += str(i)
    for j in range(1, 10):
        st1 = st
        if j is not i:
            st1 += str(j)
            for k in range(1, 10):
                st2 = st1
                if k is not  i and k is not j:
                    st2 += str(k)
                    for l in range(1, 10):
                        st3 = st2
                        if l is not  i and l is not j and l is not k:
                            st3 += str(l)
                            arr[st3] = int(st3)
                            print(st3)



count = 0
total = 0
for value in arr.values():
    total += 1
    if value % 2 is 0:
        count += 1

print(total)
print(count)
print(count/total)

