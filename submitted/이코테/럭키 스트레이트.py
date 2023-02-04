# 럭키 스트레이트

N = int(input())

length = 0
arr = []

while(True):
    div_num = (10 ** length)
    length += 1
    isDiv = N // div_num

    if isDiv == 0:
        break

    temp = (N % (div_num * 10)) // div_num
    arr.append(temp)
    

front = arr[:(length//2)]
back = arr[(length//2):]


# print(front, back)

if(sum(front) == sum(back)):
    print("LUCKY")
else:
    print("READY")
