# 문제 번호 : 1110
import sys

origin = int(sys.stdin.readline())
a = origin
cnt = 0
while True:
    ten, one = divmod(a, 10)
    sum = ten + one
    sum_ten, sum_one = divmod(sum, 10)
    a = (one * 10) + sum_one
    cnt += 1
    if a == origin:
        print(cnt)
        break
