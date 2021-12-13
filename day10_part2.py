fs = open('input.txt', 'r')
lines = list(map(str.strip, fs.readlines()))

mapping = { ')': '(', '}': '{', ']': '[', '>': '<' }
score = { ')': 1, ']': 2, '}': 3, '>': 4 }
swap_mapping = { '(': ')', '{': '}', '[': ']', '<': '>' }

ans = []
for line in lines:
    st = []
    now = 0
    invalid = False
    for ch in line:
        if ch not in mapping:
            st.append(ch)
        elif len(st) == 0 or mapping[ch] != st[-1]:
            invalid = True
            break
        elif mapping[ch] == st[-1]:
            st.pop()

    if invalid:
        continue
    
    for ch in st[::-1]:
        now = now * 5 + score[swap_mapping[ch]]

    if(now != 0):
        ans.append(now)

ans.sort()
print(ans[len(ans) // 2])