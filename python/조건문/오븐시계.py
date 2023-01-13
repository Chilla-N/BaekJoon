# 문제 번호 : 2525

a, b = map(int, input().split())
minuit = int(input())
h = minuit // 60
c = minuit % 60
b = b + c
if b >= 60:
    b -= 60
    a += 1
    if a == 24:
        a = 0
a = a + h
a = a % 24
print(str(a)+" "+str(b))
