fp = open("day1_in.txt", "r")
sum = [x*0 for x in range(1000)]
calories = fp.readlines()
elf_no = 0

for calorie in calories:
    if calorie != "\n":
        sum[elf_no] = sum[elf_no] + int(calorie)
    else:
        elf_no = elf_no + 1

sum.sort(reverse=True)
print(sum[0]+sum[1]+sum[2])