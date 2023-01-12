# 문제 번호 : 3003

normal_set = [1, 1, 2, 2, 2, 8]

input_set = list(map(int, input().split()))

result_set = []

for i in range(6):
    result_set.append(normal_set[i] - input_set[i])

result = ""

for i in result_set:
    result = result + str(i) + " "
print(result[:-1])
