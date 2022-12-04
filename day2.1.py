fp = open("day2_in.txt", "r")
mine = {'X': 1, 'Y': 2, 'Z': 3}
result = {'AX': 3, 'AY': 6, 'AZ': 0, 'BX': 0, 'BY': 3, 'BZ': 6, 'CX': 6, 'CY': 0, 'CZ': 3}

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