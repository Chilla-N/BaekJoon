# 문제 번호 : 2480

a = list(map(int, input().split()))
res = []
cnt = 1
same = 0
for i in a:
    if i in res:
        cnt += 1
        same = i
    else:
        res.append(i)
if cnt == 1:
    max_int = max(a)
    print(100 * max_int)
elif cnt == 2:
    same = same*100
    print(1000 + same)
else:
    same = same*1000
    print(10000 + same)


