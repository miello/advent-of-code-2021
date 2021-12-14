fs = open('input.txt', 'r')
lines = list(map(str.strip, fs.readlines()))

print(lines)

gamma, epsilon = '', ''

for idx in range(len(lines[0])):
    zero = 0
    one = 0
    for line in lines:
        if line[idx] == '0':
            zero += 1
        else:
            one += 1
    if zero < one:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

print(int(gamma, 2) * int(epsilon, 2))