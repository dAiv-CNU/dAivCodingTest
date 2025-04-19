# 붕어빵
answer = ""
n, _ = map(int, input().split())
for _ in range(n):
    answer += input()[::-1] + "\n"
print(answer)