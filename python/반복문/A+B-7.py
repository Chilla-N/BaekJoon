# 문제 번호 : 11021
import sys

N = int(sys.stdin.readline())

for i in range(N):
    A, B = map(int, sys.stdin.readline().split())
    print(f"Case #{i+1}: {A+B}")
