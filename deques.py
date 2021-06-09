from collections import deque

a = deque()

for _ in range(int(input())):

    l = [x for x in input().split()]

    op = ""
    e = ""

    if len(l) >= 2:
        op = l[0]
        e = l[1]
        e = int(e)
    else:
        op = l[0]

    if op == "append":
        a.append(e)
    elif op == "pop":
        a.pop()
    elif op == "popleft":
        a.popleft()
    elif op == "appendleft":
        a.appendleft(e)
    else:
        print("error")

for i in range(len(a)):
    print(a[i], end=' ')
