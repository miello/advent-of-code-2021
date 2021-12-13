fs = open('input.txt', 'r')
lines = list(map(int, fs.readlines()[0].strip().split(',')))

line = sorted(lines)
mid = (lines[len(lines) // 2] + lines[(len(lines) + 1) // 2]) // 2

mx = max(line)

dist = -1
for i in range(mx):
    mn = 0
    for j in line:
        diff = abs(j - i)

        mn += int(diff * (diff + 1) // 2)

    dist = min(mn, dist) if dist != -1 else mn

print(dist)  