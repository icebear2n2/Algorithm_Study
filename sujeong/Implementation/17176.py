import sys

lst = [' ']
n = int(sys.stdin.readline())
char_num = list(map(int, sys.stdin.readline().split()))
str = list(sys.stdin.readline())
str.remove('\n')


lst3 = []
for i in range(65, 123):
    if i > 90 and i < 97:
        continue
    else:
        lst.append(chr(i))

for i in char_num:
    lst3.append(lst[i])

if str[-1] != ' ' and str[0] != ' ':
    str.sort()
    lst3.sort()
    if str == lst3:
        print("y")
    else:
        print("n")
else:
    print("n")

