import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
lst2 = list()
lst.sort()
result = 0
for i in range(1, n+1):
    result += lst[i-1]

    lst2.append(result)

print(sum(lst2))