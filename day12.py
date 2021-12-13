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
def dfs(now: str, chk: set[str]):
    if now == 'end':
        global cnt
        cnt += 1
        return

    if now.islower():
        chk.add(now)
    
    for end in edges[now]:
        if end not in chk:
            dfs(end, chk.copy())
    
dfs('start', set())
print(cnt)

