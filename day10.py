fs = open('input.txt', 'r')
lines = list(map(str.strip, fs.readlines()))

mapping = { ')': '(', '}': '{', ']': '[', '>': '<' }
score = { ')': 3, ']': 57, '}': 1197, '>': 25137 }

ans = 0
for line in lines:
    st = []
    for ch in line:
        if ch not in mapping:
            st.append(ch)
        elif mapping[ch] != st[-1]:
            ans += score[ch]
            break     
        else:
            st.pop()
print(ans)