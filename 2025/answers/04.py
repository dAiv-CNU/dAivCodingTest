# 16진수

s = input()
hex_ = "0123456789ABCDEF"
result = 0
for i, digit in enumerate(s[::-1]):
    result += hex_.index(digit) * 16**i
print(result)
