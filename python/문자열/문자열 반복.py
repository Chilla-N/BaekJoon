# 문제 번호 : 2675
n = int(input())


for i in range(n):
    repeat, word = input().split()
    repeat = int(repeat)
    result = ""
    for c in word:
        result += c * repeat
    print(result)
