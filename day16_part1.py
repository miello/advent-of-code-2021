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

def parse(data, st, ed):
    if st + 2 >= ed:
        return ed
    v = int(data[st:st + 3], 2)
    if st + 5 >= ed:
        return ed
    t = int(data[st + 3: st + 6], 2)

    if t == 4:
        i = st + 6
        while True:
            if i + 5 > ed:
                break
            tmp = data[i:i+5]
            i += 5
            if tmp[0] == '0':
                break
        return i, v

    i = int(data[st + 6], 2)
    if i == 0:
        length = int(data[st + 7:st + 22], 2)

        now_version = v
        x = st + 22
        while x < st + 22 + length:
            x, _v = parse(data, x, st + 22 + length)
            now_version += _v
        return st + 22 + length, now_version
    else:
        num = int(data[st + 7:st + 18], 2)
        x = st + 18
        now_version = v

        while num != 0:
            x, _v = parse(data, x, ed)
            now_version += _v
            num -= 1       
        return x, now_version

print(parse(bits, 0, len(bits))[1])