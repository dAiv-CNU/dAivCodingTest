# 종민이의 첫사랑

stroke_lst = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
stroke_a = [stroke_lst[ord(i)-65] for i in input()]
stroke_b = [stroke_lst[ord(i)-65] for i in input()]
lst = []

for i in range(len(stroke_a)):
    lst += [stroke_a[i], stroke_b[i]]

while len(lst) != 2:
    next_lst = []
    for i in range(len(lst)-1):
        next_lst.append((lst[i]+lst[i+1]) % 10)
    lst = next_lst

print(f"{lst[0]}{lst[1]}")
