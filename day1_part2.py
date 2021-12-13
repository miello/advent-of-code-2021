fs = open('input.txt', 'r')
num = list(map(int, list(fs.readlines())))

prev = None
ans = 0

sum_three = []

for i in range(len(num) - 2):
    now = 0    
    for j in range(3):
        now += num[i + j]
    sum_three.append(now)

for i in sum_three:
    if prev is None:
        prev = i
    else:
        ans += (prev < i)
    prev = i

print(ans)