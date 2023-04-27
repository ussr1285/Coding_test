N = int(input())
integers = list(map(int, input().split(" ")))
v = int(input())

cnt = 0

for elem in integers:
    if(elem == v):
        cnt += 1

print(cnt)