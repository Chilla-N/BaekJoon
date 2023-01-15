# 문제 번호 : 10871
import sys

N, X = map(int, sys.stdin.readline().rstrip().split())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
result = ""
for i in nums:
    if X > i:
        result += str(i)+" "
print(result[:-1])
