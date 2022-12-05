fp = open("day3_in.txt", "r")
items = fp.readlines()

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

points = 0
i = 0
for i in range(0, len(items), 3):
    first = items[i+0]
    second = items[i+1]
    third = items[i+2]
    unique, = set(first).intersection(set(second), set(third)) - set('\n')
    if unique in lowercase:
        points += lowercase.index(unique) + 1
    elif unique in uppercase:
        points += uppercase.index(unique) + 27
    
print(points)