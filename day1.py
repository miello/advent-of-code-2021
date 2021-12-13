fs = open('input.txt', 'r')
num = list(map(int, list(fs.readlines())))

prev = None
ans = 0

for i in num:
    if prev is None:
        prev = i
    else:
        ans += (prev < i)
    prev = i

print(ans)