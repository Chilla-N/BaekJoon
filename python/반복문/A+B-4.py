# 문제 번호 : 10951
import sys

while True:
    try:
        A, B = map(int, sys.stdin.readline().rstrip().split())
        print(A+B)
    except ValueError:
        break
