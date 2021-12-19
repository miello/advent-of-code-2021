fs = open('input.txt', 'r')
bitStream = fs.readline().strip()

bits = ''
for hex in bitStream:
    now = int(hex, 16)
    bit = ""
    for i in range(4):
        bit += str(now & 1)
        now //= 2
    bits += bit[::-1]

packet = []

def parse(data, st, ed, isInside):
    if st + 2 >= ed:
        return ed
    v = int(data[st:st + 3], 2)
    if st + 5 >= ed:
        return ed
    t = int(data[st + 3: st + 6], 2)

    if t == 4:
        i = st + 6
        _tmp = [(v, t)]
        st = ""
        while True:
            if i + 5 > ed:
                break
            tmp = data[i:i+5]
            i += 5
            st += tmp[1:]
            if tmp[0] == '0':
                break
        _tmp.append(int(st, 2))
        return i, _tmp

    i = int(data[st + 6], 2)
    if i == 0:
        length = int(data[st + 7:st + 22], 2)
        tmp = [(v, t)]

        x = st + 22
        while x < st + 22 + length:
            x, l = parse(data, x, st + 22 + length, True)
            tmp.append(l)

        if not isInside:
            packet.append(tmp)
        return st + 22 + length, tmp
    else:
        num = int(data[st + 7:st + 18], 2)
        x = st + 18

        tmp = [(v, t)]
        while num != 0:
            x, l = parse(data, x, ed, True)
            tmp.append(l)
            num -= 1       

        if not isInside:
            packet.append(tmp)
        return x, tmp

def calculate(data):
    operator = data[0][1]
    num = []
    for each in data[1:]:
        if isinstance(each, list):
            num.append(calculate(each))
        else:
            num.append(each)
    if operator == 0:
        return sum(num)
    elif operator == 1:
        now = 1
        for j in num:
            now *= j
        return now
    elif operator == 2:
        return min(num)
    elif operator == 3:
        return max(num)
    elif operator == 4:
        return num[0]
    elif operator == 5:
        return int(num[0] > num[1])
    elif operator == 6:
        return int(num[0] < num[1])
    elif operator == 7:
        return int(num[0] == num[1])

parse(bits, 0, len(bits), False)

print(calculate(packet[0]))