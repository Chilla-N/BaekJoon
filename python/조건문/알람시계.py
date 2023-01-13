# 문제 번호 : 2884

a, b = map(int, input().split())

if b >= 45:
    b = b -45
else:
    b = b + 15
    if a == 0:
        a = a + 23
    else:
        a = a - 1

print(str(a)+" "+str(b))