import sys

n, m = map(int,sys.stdin.readline().split())
result=[]

for i in range(0, n):
    lst = list(map(int, sys.stdin.readline().split()))
    if len(lst) > m:
        print('error')
        break

    lst.sort()
    result.append(lst[0])

    result.sort()

print(result[-1])