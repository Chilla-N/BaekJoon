# 문제 번호 : 3052

res = []
for i in range(10):
    a = int(input()) % 42
    if a not in res:
        res.append(a)
print(len(res))
