# 문제 번호 : 5597


a = [1 for i in range(30)]

for i in range(28):
    a[int(input())-1] = 0
b = a.index(1)
print(b+1)
a[b] = 0
print(a.index(1)+1)
