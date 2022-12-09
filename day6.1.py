fp = open("day6_in.txt", "r")
stream = fp.readline()
i = 0
while (i<len(stream)):
    li = []
    li.append(stream[i])
    li.append(stream[i+1])
    li.append(stream[i+2])
    li.append(stream[i+3])
    unique = set(li)

    if len(unique)!=len(li):
        i += 1
    else:
        break

print(i+4)