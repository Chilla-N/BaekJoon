# 문제 번호 : 10809

word = input()

a = [-1 for i in range(26)]

for i, character in enumerate(word):
    if a[ord(character)-97] == -1:
        a[ord(character) - 97] = i

result = ""
for i in a:
    result += str(i) + " "
print(result[:-1])
