# 문제 번호 : 8958

n = int(input())

for i in range(n):
    entire_score = 0
    res = 0
    ox = input()
    for score in list(ox):
        if score == "O":
            res += 1
            entire_score += res
        else:
            res = 0
    print(entire_score)