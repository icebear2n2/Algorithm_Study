import sys

n, m, k = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

data = sorted(data)

first = data[n-1]
second = data[n-2]

result = first * k
result += second
result *= int(m / (k + 1))

print(result)