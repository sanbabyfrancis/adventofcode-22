fp = open("day2_in.txt", "r")
mine = {'X': 0, 'Y': 3, 'Z': 6}
result = {'AX': 3, 'AY': 1, 'AZ': 2, 'BX': 1, 'BY': 2, 'BZ': 3, 'CX': 2, 'CY': 3, 'CZ': 1}

points = 0
outcomes = fp.readlines()
for i in outcomes:
    if i[0]=='A' and i[2]=='X':
        points += mine[i[2]] + result[i[0]+i[2]]
    elif i[0]=='A' and i[2]=='Y':
        points += mine[i[2]] + result[i[0]+i[2]]
    elif i[0]=='A' and i[2]=='Z':
        points += mine[i[2]] + result[i[0]+i[2]]
    elif i[0]=='B' and i[2]=='X':
        points += mine[i[2]] + result[i[0]+i[2]]
    elif i[0]=='B' and i[2]=='Y':
        points += mine[i[2]] + result[i[0]+i[2]]
    elif i[0]=='B' and i[2]=='Z':
        points += mine[i[2]] + result[i[0]+i[2]]
    elif i[0]=='C' and i[2]=='X':
        points += mine[i[2]] + result[i[0]+i[2]]
    elif i[0]=='C' and i[2]=='Y':
        points += mine[i[2]] + result[i[0]+i[2]]
    elif i[0]=='C' and i[2]=='Z':
        points += mine[i[2]] + result[i[0]+i[2]]
    
print(points)