# 문제 번호 : 10818
import sys

input()
nums = list(map(int, sys.stdin.readline().rstrip().split()))
print(str(min(nums))+" "+str(max(nums)))
