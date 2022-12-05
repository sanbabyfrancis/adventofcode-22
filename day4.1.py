fp = open("day4_in.txt", "r")
pair_li = fp.readlines()

count = 0
for pair in pair_li:
    first, second = pair.split(",")
    fi_one, fi_two = [int(x) for x in first.split("-")]
    sec_one, sec_two = [int(x) for x in second.split("-")]
    if fi_one <= sec_one <= sec_two <= fi_two:
        count = count + 1
    elif sec_one <= fi_one <= fi_two <= sec_two:
        count = count + 1

print(count)