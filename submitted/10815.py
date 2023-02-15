N = int(input())
N_arr = set(map(int, input().split(" "))) # 처음에 그냥 리스트로 했다가, 시간 초과로 틀림.
M = int(input())
M_arr = list(map(int, input().split(" ")))
result_arr = []

for num in M_arr:
    if(num in N_arr):
      result_arr.append(1)
    else:
      result_arr.append(0)
for num in result_arr:
    print(num, end=" ")