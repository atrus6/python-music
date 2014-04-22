file = open('test.csv', 'r')
output = open('cleaned-C.csv', 'w')

for line in file:
    sp = line.split()
    num = int(sp[0])
    if num  >= 0 and num <= 12:
        output.write(line)

