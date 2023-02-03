X = int(input())

index = 1
w = 1 # 몇번째 대각선 칸

A = 1 # 분자
B = 1 # 분모

if(X != 1):
    while(index < X):
        w += 1
        index += w

    dis = index - X

    if w % 2 == 0:
        A = w
        A -= dis
        B += dis
    else: 
        B = w
        A += dis
        B -= dis

print(str(A)+"/"+str(B))
