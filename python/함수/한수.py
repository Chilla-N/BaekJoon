# 문제 번호 : 1065

def check_diff(diff, i):
    for k in range(len(i) - 1):
        if diff != (int(i[k]) - int(i[k + 1])):
            return False
    return True


n = int(input())

cnt = 0
for i in range(1, n + 1):
    if i < 100:
        cnt += 1
        continue
    i = str(i)
    diff = int(i[0]) - int(i[1])
    if check_diff(diff, i):
        cnt += 1
print(cnt)