import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
lst2 = list()
lst.sort()
result = 0
for i in lst:
    result += i
    
    lst2.append(result)

print(sum(lst2))
