# 문제 번호 : 4344

c = int(input())
for k in range(c):
    gets = list(map(int, input().split()))
    n = gets[0]
    student = gets[1:]
    mean = sum(student)/len(student)
    cnt = 0
    for st in student:
        if st > mean:
            cnt += 1
    per = str(round(cnt * 100 / n, 3))
    zero = len(per.split(".")[1])
    if zero != 3:
        per = per + (3-zero)*"0"
    print(per+"%")
