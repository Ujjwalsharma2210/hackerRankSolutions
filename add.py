# This program uses set to identify the number of unique countries entered.

print(len(set([str(input()) for x in range(int(input()))])))
