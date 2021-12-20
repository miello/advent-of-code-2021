from math import sqrt

fs = open('input.txt', 'r')
line = fs.readline().split()

x = line[2][2:-1].split('..')
y = line[3][2:].split('..')

min_x = int(x[0])
max_x = int(x[1])

min_y = int(y[0])
max_y = int(y[1])

def isValid(h, x, min_y, max_y, min_x, max_x):
    nowH = 0
    nowX = 0
    sub = 1
    if h < 0:
        sub = -h        
    while h >= 0:
        nowH += h
        nowX += x
        if min_y <= nowH and nowH <= max_y and min_x <= nowX and nowX <= max_x:
            return True
        h -= 1
        if x > 0:
            x -= 1
        elif x < 0:
            x += 1
    while min_y < nowH:
        nowH -= sub
        nowX += x
        if min_y <= nowH and nowH <= max_y and min_x <= nowX and nowX <= max_x:
            return True
        sub += 1
        if x > 0:
            x -= 1
        elif x < 0:
            x += 1
    return False

cnt = 0
# Brute Force Method (Not efficient)
for i in range(-500, 500):
    for j in range(-250, 250):
        if isValid(i, j, min_y, max_y, min_x, max_x):
            cnt += 1

print(cnt)
