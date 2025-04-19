#농구 한판 할까
n = int(input())
lst = [input().split() for i in range(n)]
lst.append(["0", "48:00"])
previous_time, point, a_time, b_time = 0, 0, 0, 0
for i in range(n+1):
    current_time = 60 * int(lst[i][1][:2]) + int(lst[i][1][3:])
    if point > 0:
        a_time += current_time-previous_time
    elif point < 0:
        b_time += current_time-previous_time
    if lst[i][0] == '1':
        point += 1
    elif lst[i][0] == '2':
        point -= 1
    previous_time = current_time
print("%02d:%02d" % (a_time//60, a_time % 60))
print("%02d:%02d" % (b_time//60, b_time % 60))
