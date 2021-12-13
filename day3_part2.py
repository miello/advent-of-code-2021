fs = open('input.txt', 'r')
lines = list(map(str.strip, fs.readlines()))

gamma, epsilon = '', ''

x = lines[:]
for idx in range(len(lines[0])):
    zero = 0
    one = 0
    if len(x) == 1:
        break
    for line in x:
        if line[idx] == '0':
            zero += 1
        else:
            one += 1
    y = []
    if zero <= one:
        for line in x:
            if line[idx] == '1':
                y.append(line)
    else:
        for line in x:
            if line[idx] == '0':
                y.append(line)
    x = y[:]

gamma = x[0]
x = lines[:]
for idx in range(len(lines[0])):
    zero = 0
    one = 0
    if len(x) == 1:
        break
    for line in x:
        if line[idx] == '0':
            zero += 1
        else:
            one += 1
    y = []
    if zero <= one:
        for line in x:
            if line[idx] == '0':
                y.append(line)
    else:
        for line in x:
            if line[idx] == '1':
                y.append(line)
    x = y[:]

epsilon = x[0]

print(gamma, epsilon)
print(int(gamma, 2) * int(epsilon, 2))