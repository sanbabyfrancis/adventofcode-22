fp = open("day6_in.txt", "r")
stream = fp.readline()
i = 0
while (i<len(stream)):
    li = []
    for j in range(14):
        li.append(stream[j+i])
    unique = set(li)

    if len(unique)!=len(li):
        i += 1
    else:
        break

print(i+14)