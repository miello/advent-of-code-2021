fs = open('input.txt', 'r')

edges: dict[str, list[str]] = {}
lines = list(map(lambda x: x.strip().split('-'), fs.readlines()))

for (st, ed) in lines:
    if st not in edges:
        edges[st] = []
    if ed not in edges:
        edges[ed] = []
    edges[st].append(ed)
    edges[ed].append(st)

cnt = 0
def dfs(now: str, chk: dict[str, int], isTwice: bool):
    if now == 'end':
        global cnt
        cnt += 1
        return

    if now.islower():
        if now not in chk:
            chk[now] = 0
        chk[now] += 1
        if chk[now] == 2:
            isTwice = True
    
    for end in edges[now]:
        if end == 'start':
            continue
        foundTwiceCase = isTwice and end not in chk
        notFoundTwice = not isTwice and (end not in chk or chk[end] != 2)
        if foundTwiceCase or notFoundTwice:
            dfs(end, chk.copy(), isTwice)
    
dfs('start', dict(), False)
print(cnt)

