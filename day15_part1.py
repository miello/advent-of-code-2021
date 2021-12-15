from collections import deque
fs = open('input.txt', 'r')

lines = list(map(lambda x: list(map(int, list(x.strip()))), fs.readlines()))
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