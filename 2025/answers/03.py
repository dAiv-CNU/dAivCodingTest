# 종이 접기

n = int(input())
sum_ = 0
for _ in range(n):
    sum_ += sum(map(int, input().split()))

print(sum_)


#print(sum([sum(map(int,input().split()))for _ in range(int(input()))]))
