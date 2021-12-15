from collections import deque


fs = open('input.txt', 'r')
lines = list(map(lambda x: list(map(int, list(x.strip()))), fs.readlines()))

for i in range(len(lines)):
    rowSz = len(lines[i])
    for cnt in range(1, 5):
        for j in range(rowSz):
            newVal = lines[i][j] + cnt
            if newVal > 9:
                newVal %= 9
            lines[i].append(newVal)


colSz = len(lines)
for cnt in range(1, 5):
    for i in range(colSz):
        cpy = lines[i][:]
        for j in range(len(cpy)):
            cpy[j] += cnt
            if cpy[j] > 9:
                cpy[j] %= 9
        lines.append(cpy)

sz = len(lines)

q = deque()
q.append((0, 0))

mov = [[0, 1], [1, 0], [-1, 0], [0, -1]]

dp = [[-1 for i in range(sz)] for j in range(sz)]

dp[0][0] = 0

while len(q) != 0:
    x, y = q.popleft()
    if dp[x][y] == -1:
        continue
    for (dx, dy) in mov:
        newX = x + dx
        newY = y + dy
        if newX >= 0 and newY >= 0 and newX < sz and newY < sz:
            if dp[newX][newY] > dp[x][y] + lines[newX][newY] or dp[newX][newY] == -1:
                dp[newX][newY] = dp[x][y] + lines[newX][newY]
                q.append((newX, newY))

print(dp[sz - 1][sz - 1])