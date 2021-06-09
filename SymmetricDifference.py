

n = int(input())
lis1 = [int(x) for x in input().split()]
set1 = set(lis1)

m = int(input())
lis2 = [int(x) for x in input().split()]
set2 = set(lis2)

set3 = set1.union(set2) - set1.intersection(set2)
set3 = sorted(set3)

for el in set3:
    print(el, end='\n')

# print(set1)
