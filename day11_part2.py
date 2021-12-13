from collections import deque
fs = open('input.txt', 'r')

energy = list(map(lambda x: list(map(int, list(x.strip()))), fs.readlines()))

round = 0
row = len(energy)
col = len(energy[0])

cnt = -1
while cnt != 0:
    cnt = 0
    round += 1
    flash = []
    check = [[False for e in range(col)] for _e in range(row)]
    for j in range(row):
        for k in range(col):
            energy[j][k] += 1
            if energy[j][k] > 9:
                flash.append((j, k))
    
    while len(flash) != 0:
        x, y = flash[len(flash) - 1]
        flash.pop()

        if check[x][y]:
            continue
        
        check[x][y] = True
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx == 0 and dy == 0:
                    continue
                newX = x + dx
                newY = y + dy
                if newX >= 0 and newX < row and newY >= 0 and newY < col:
                    energy[newX][newY] += 1
                    if energy[newX][newY] > 9:
                        flash.append((newX, newY))

    for j in range(row):
        for k in range(col):
            if energy[j][k] > 9:
                energy[j][k] = 0
    
    for j in range(row):
        for k in range(col):
            cnt += energy[j][k] != 0
    
print(round)