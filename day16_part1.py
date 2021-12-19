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
        parse_data = []
        while True:
            if i + 5 > ed:
                break
            tmp = data[i:i+5]
            i += 5
            parse_data.append(tmp)
            if tmp[0] == '0':
                break
        packet.append((v, t, parse_data))
        return i

    i = int(data[st + 6], 2)
    if i == 0:
        length = int(data[st + 7:st + 22], 2)
        packet.append((v, t))

        x = st + 22
        while x < st + 22 + length:
            x = parse(data, x, st + 22 + length)
        return st + 22 + length
    else:
        num = int(data[st + 7:st + 18], 2)
        x = st + 18

        packet.append((v, t))
        while num != 0:
            x = parse(data, x, ed)
            num -= 1       
        return x

parse(bits, 0, len(bits))
version = 0

for each in packet:
    version += each[0]
print(version)
print(packet)