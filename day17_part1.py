fs = open('input.txt', 'r')
line = fs.readline().split()

x = line[2][2:-1].split('..')
y = line[3][2:].split('..')

min_x = int(x[0])
max_x = int(x[1])

min_y = int(y[0])
max_y = int(y[1])

def isValidY(h, min_y, max_y):
    nowH = 0
    t = 0
    while h >= 0:
        nowH += h
        if min_y <= nowH and nowH <= max_y:
            return True
        h -= 1
        t += 1
    sub = 1
    while min_y < nowH:
        nowH -= sub
        if min_y <= nowH and nowH <= max_y:
            return True
        sub += 1
        t += 1
    return False

testH = 0
# Brute Force Method (Not efficient)
for i in range(1000):
    if isValidY(i, min_y, max_y):
        testH = i

print(testH * (testH + 1) // 2)
