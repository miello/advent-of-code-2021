fs = open('input.txt', 'r')
lines = fs.readlines()

depth = 0
horizontal = 0
aim = 0

for line in lines:
    word, dist = line.strip().split()
    dist = int(dist)

    if word == "forward":
        horizontal += dist
        depth += dist * aim
        pass
    if word == "down":
        aim += dist
        pass
    if word == "up":
        aim -= dist
        pass

    aim = max(0, aim)

print(depth * horizontal)