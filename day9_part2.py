fs = open('input.txt', 'r')
lines = list(map(lambda x: list(map(int, list(x.strip()))), fs.readlines()))

diff = [(-1, 0), (0, -1), (1, 0), (0, 1)]

ans = 0
row = len(lines)
col = len(lines[0])

def recur(x, y):
    ans = 0
    for (dx, dy) in diff:
        if x + dx >= 0 and x + dx < row and y + dy >= 0 and y + dy < col:
            if lines[x + dx][y + dy] != 9:
                lines[x + dx][y + dy] = 9
                ans += recur(x + dx, y + dy)
    return ans + 1

pos = []

for i in range(row):
    for j in range(col):
        valid = True
        for (dx, dy) in diff:
            if i + dx >= 0 and i + dx < row and j + dy >= 0 and j + dy < col:
                valid &= lines[i][j] < lines[i + dx][j + dy]
        if valid:
            pos.append((i, j))

ans = []
for (x, y) in pos:
    ans.append(recur(x, y) - 1)

ans.sort(reverse=True)
print(ans[0] * ans[1] * ans[2])