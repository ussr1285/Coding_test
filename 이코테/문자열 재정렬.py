# 문자열 재정렬

input_ = input()

num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

input_chr = []
input_num = []

for chr in input_:
    if chr in num:
        input_num.append(chr)
    else:
        input_chr.append(chr)

input_num.sort()
input_chr.sort()

print(input_chr + input_num)

