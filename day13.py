# Part 1
fs = open('input.txt', 'r')
lines = fs.readlines()

pos: set[(int, int)] = set()
test = 0
for line in lines:
    test += 1
    if line.strip() != '':
        line = list(map(int, line.strip().split(',')))
        pos.add((line[0], line[1]))
    else:
        break

for i in range(test, len(lines)):
    flipStr = lines[i].split()[2].split('=')
    direction = flipStr[0]
    r = int(flipStr[1])

    newPos = set()
    if direction == 'x':
        for (x, y) in pos:
            if x > r:
                newPos.add((x - 2 * (x - r), y))
            else:
                newPos.add((x, y))
        pos = newPos.copy()
    elif direction == 'y':
        for (x, y) in pos:
            if y > r:
                newPos.add((x, y - 2 * (y - r)))
            else:
                newPos.add((x, y))
        pos = newPos.copy()

# Part 2
w = 0
h = 0
for (x, y) in pos:
    w = max(w, x)
    h = max(h, y)

for j in range(h + 1):
    for i in range(w + 1):
        # Great Tips from https://www.reddit.com/r/adventofcode/comments/rf7onx/comment/hocyv3b/?utm_source=reddit&utm_medium=web2x&context=3
        print('\u2593' if (i, j) in pos else '\u2591', end="")
    print()