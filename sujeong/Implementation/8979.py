import sys
n, num = map(int,sys.stdin.readline().split())

dic = {}
count = 0

for i in range(1, n+1):
    
    lst = list(map(int,sys.stdin.readline().split()))
    dic[lst.pop(0)] = lst

dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)

for i in range(1, len(dic)+1):
    if dic[i-1][0] == num:
        count+=1
        break
    else:
        if dic[i-1][1] == dic[i][1]:
            continue
        else:
            count += 1
            
print(count)