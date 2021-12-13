fs = open('input.txt', 'r')
lines = list(map(lambda x: list(map(int, list(x.strip()))), fs.readlines()))

diff = [(-1, 0), (0, -1), (1, 0), (0, 1)]

ans = 0
row = len(lines)
col = len(lines[0])

for i in range(row):
    for j in range(col):
        valid = True
        for (dx, dy) in diff:
            if i + dx >= 0 and i + dx < row and j + dy >= 0 and j + dy < col:
                valid &= lines[i][j] < lines[i + dx][j + dy]
        if valid:
            ans += lines[i][j] + 1

print(ans)