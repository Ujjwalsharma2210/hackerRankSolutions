s = set()

n = int(input())
lis = input().split()
for ele in lis:
    s.union(ele)

m = int(input())
li = input().split()
for ele in li:
    s.union(ele)

print(len(s))
