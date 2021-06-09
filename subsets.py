bools = []

for _ in range(int(input())):

    status = None

    nA = int(input())
    a = set([int(x) for x in input().split()])

    nB = int(input())
    b = set([int(y) for y in input().split()])

    if a.issubset(b):
        bools.append(True)
    else:
        bools.append(False)


for e in bools:
    print(e, end='\n')
