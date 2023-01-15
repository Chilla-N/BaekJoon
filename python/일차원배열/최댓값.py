# 문제 번호 : 2562

max = 0
for i in range(9):
    a = int(input())
    if a > max:
        max = a
        cnt = i+1
print(max)
print(cnt)


