fs = open('input.txt', 'r')
lines = fs.readlines()

row = 0
col = 0

for i in range(len(lines)):
    st, ed = lines[i].split('->')
    st = list(map(int, st.split(',')))
    ed = list(map(int, ed.split(',')))

    row = max(row, st[0], ed[0])
    col = max(col, st[1], ed[1])

    lines[i] = (st, ed)

found = [[0 for _ in range(col + 1)] for _ in range(row + 1)]

for (st, ed) in lines:
    row_inc = -1 if st[0] - ed[0] > 0 else (1 & int(st[0] != ed[0]))
    col_inc = -1 if st[1] - ed[1] > 0 else (1 & int(st[1] != ed[1]))

    if row_inc != 0 and col_inc != 0:
        continue

    while True:
        found[st[0]][st[1]] += 1
        if st[0] == ed[0] and st[1] == ed[1]:
            break
        st[0] += row_inc
        st[1] += col_inc

ans = 0
for i in found:
    for j in i:
        ans += int(j >= 2)

print(ans)