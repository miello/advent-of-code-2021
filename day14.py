# Solution for both part 1 and 2
fs = open('input.txt', 'r')

lines = list(map(str.strip, fs.readlines()))
polymer = lines[0]
data = dict()
rules = dict()
cnt = dict()

for line in lines[2:]:
    st, ed = line.split('->')
    st = st.strip()
    ed = ed.strip()

    rules[st] = ed

for i in polymer:
    if i not in cnt:
        cnt[i] = 0
    cnt[i] += 1

for i in range(len(polymer) - 1):
    val = polymer[i:i + 2]

    if val not in data:
        data[val] = 0
    data[val] += 1

step = int(input('How many step that want to calculate ?: '))

while step != 0:
    step -= 1
    newData = dict()
    for (key, val) in data.items():
        if key in rules:
            out_1 = key[0] + rules[key]
            out_2 = rules[key] + key[1]

            if out_1 not in newData:
                newData[out_1] = 0

            if out_2 not in newData:
                newData[out_2] = 0

            if rules[key] not in cnt:
                cnt[rules[key]] = 0

            cnt[rules[key]] += val
            newData[out_1] += val
            newData[out_2] += val   
        else:
            newData[key] = val

    data = newData.copy()

val = cnt.values()
print(max(val) - min(val))