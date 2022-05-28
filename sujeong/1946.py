import sys
import time

start = time.time()
t = int(sys.stdin.readline())

while True:
    lst = []
    count = 0
    n = int(sys.stdin.readline())
    for i in range(1, n+1):
        n1, n2 = map(int, sys.stdin.readline().split())
        lst.append(n1)
        lst.append(n2)
        if sorted(lst)[-1] <= n1 or sorted(lst)[-1] <= n2:
            count += 1
        else:
            continue

    print(count)
    print("time :", time.time() - start)


