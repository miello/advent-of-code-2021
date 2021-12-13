# Solution for both part 1 and 2
fs = open('input.txt', 'r')
line = fs.readlines()[0]

allFish = list(map(int, line.split(',')))

day = int(input('How many day that want to calculate: '))

cntFish = [0 for i in range(9)]

for i in allFish:
    cntFish[i] += 1

while day != 0:
    day -= 1
    add = 0
    newFish = [0 for i in range(9)]
    for i in range(9):
        if i == 0:
            newFish[8] += cntFish[0]
            newFish[6] += cntFish[0]
        else:
            newFish[(i + 7) % 8] += cntFish[i]
    
    for i in range(9):
        cntFish[i] = newFish[i]
    
print(sum(cntFish))