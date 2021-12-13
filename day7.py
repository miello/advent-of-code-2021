fs = open('input.txt', 'r')
lines = list(map(int, fs.readlines()[0].strip().split(',')))

line = sorted(lines)
mid = (line[len(line) // 2] + line[(len(line) + 1) // 2]) // 2

dist = 0
for j in line:
    dist += abs(j - mid)

print(dist)  