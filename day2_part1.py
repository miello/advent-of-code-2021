fs = open('input.txt', 'r')
lines = fs.readlines()

depth = 0
horizontal = 0

for line in lines:
    word, dist = line.strip().split()
    dist = int(dist)

    if word == "forward":
        horizontal += dist
        pass
    if word == "down":
        depth += dist
        pass
    if word == "up":
        depth -= dist
        pass


print(depth * horizontal)