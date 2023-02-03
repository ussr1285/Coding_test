A, B, C = list(map(int, input().split(" ")))

profit = C - B

if(profit > 0):

    cnt = A / profit

    if B % profit >= 0:

        cnt += 1

else:

    cnt = -1

print(int(cnt))

