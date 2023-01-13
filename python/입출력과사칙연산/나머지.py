# 문제 번호 : 10430

A, B, C = map(int, input().split())
a = A+B
print(a % C)
a = A%C
b = B%C
print((a + b)%C)
a = A*B
print(a%C)
a = A%C
b = B%C
c = a*b
print(c%C)
