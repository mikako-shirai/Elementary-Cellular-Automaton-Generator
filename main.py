
decimal_num = input('rule number (0-255) : ')
row = int(input("number of row (hit enter to skip) : ") or "200")
column = int(input("number of column (hit enter to skip) : ") or "400") // 2

binary_num = bin(int(decimal_num))[2:]
if len(binary_num) < 8:
    binary_num = '0' * (8-len(binary_num)) + binary_num

combinations = ['111', '110', '101', '100', '011', '010', '001', '000']
rule = {}
for (combination, digit) in zip(combinations, binary_num):
    rule[combination] = digit


neighbors = []
result = ['0'] * column + ['1'] + ['0'] * column
length = len(result)

for i in range(row):
    with open('rule_{}.txt'.format(decimal_num), mode='a') as f:
        f.writelines(' '.join(result) + '\n')
    neighbors, result = result, []
    
    for j in range(length):
        if j == 0:
            result.append(rule['{}{}{}'.format(neighbors[-1], neighbors[j], neighbors[j+1])])
        elif j == length-1:
            result.append(rule['{}{}{}'.format(neighbors[j-1], neighbors[j], neighbors[0])])
        else:
            result.append(rule['{}{}{}'.format(neighbors[j-1], neighbors[j], neighbors[j+1])])
