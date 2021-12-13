def isWin(x):
    for i in range(5):
        for j in range(5):
            rowTrue, columnTrue = True, True
            for k in range(5):
                rowTrue &= (x[i][k] == '')
            for k in range(5):
                columnTrue &= (x[k][j] == '')
            if rowTrue or columnTrue:
                return True

    return False

fs = open('input.txt', 'r')

lines = list(map(str.strip, fs.readlines()))

bingoBall = lines[0].split(',')
bingoTableList = lines[2:]
bingoTable = []

now = []
for i in range(0, len(bingoTableList), 6):
    bingoTable.append(list(map(lambda x: x.split(), bingoTableList[i:i + 5])))

lastWinner = 0
for i in bingoBall:
    for table in bingoTable:
        for k in range(5):
            for l in range(5):
                if table[k][l] != '' and i == table[k][l]:
                    table[k][l] = ''
    win = 0
    p = 0
    for table in bingoTable:
        win += int(isWin(table))

    if win == len(bingoTable) - 1:
        foundLastWinner = True
        for i in range(len(bingoTable)):
            if not isWin(bingoTable[i]):
                lastWinner = i
                
    elif win == len(bingoTable):
        s = 0
        for k in range(5):
            for l in range(5):
                if bingoTable[lastWinner][k][l] != '':
                    s += int(bingoTable[lastWinner][k][l])
        print(int(i) * s)
        break