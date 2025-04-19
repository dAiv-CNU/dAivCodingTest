# 좌표 압축

_ = int(input())
pos_arr = list(map(int, input().split()))
sorted_unique_pos = sorted(set(pos_arr))
pos_map = dict(zip(sorted_unique_pos, range(len(sorted_unique_pos))))
result = [pos_map[pos] for pos in pos_arr]
print(*result)
