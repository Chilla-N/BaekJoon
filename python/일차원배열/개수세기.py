# 문제 번호 : 10807
import sys

N = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
target = int(sys.stdin.readline().rstrip())
print(nums.count(target))