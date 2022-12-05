fp = open("day4_in.txt", "r")
pair_li = fp.readlines()

count = 0
for pair in pair_li:
    first, second = pair.split(",")
    fi_one, fi_two = [int(x) for x in first.split("-")]
    sec_one, sec_two = [int(x) for x in second.split("-")]
    if set(range(fi_one, fi_two+1)).intersection(set(range(sec_one, sec_two+1))) != set():
        count = count + 1

print(count)