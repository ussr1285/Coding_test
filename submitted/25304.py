X = int(input())
N = int(input())

total = 0
a = 0
b = 0

for _ in range(N):
    a, b = list(map(int, input().split(" ")))
    total += a*b


if(X == total):
    print("Yes")
else:
    print("No")
