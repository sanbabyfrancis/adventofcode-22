fp = open("day3_in.txt", "r")
items = fp.readlines()

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

points = 0
for line in items:
    first = line[0:len(line)//2]
    second = line[len(line)//2::]
    unique, = set(first).intersection(set(second))
    if unique in lowercase:
        points += lowercase.index(unique) + 1
    elif unique in uppercase:
        points += uppercase.index(unique) + 27
    
print(points)