# 홀수

arr = [int(input()) for _ in range(7)]
odd_arr = [i for i in arr if i % 2]
if odd_arr:
    print(sum(odd_arr))
    print(min(odd_arr))
else:
    print(-1)
##########################################################################
# arr = []
# for i in range(7):
#     arr.append(int(input()))

# odd_arr = []
# for i in arr:
#     if i % 2 == 0:
#         odd_arr.append(i)

# if len(odd_arr) != 0:
#     print(sum(odd_arr))
#     print(min(odd_arr))
# else:
#     print(-1)
