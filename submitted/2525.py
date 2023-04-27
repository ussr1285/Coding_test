now = list(map(int, input().split(" ")))
cook_time = int(input())

temp_time = now[0]*60 + now[1] + cook_time

hour = (temp_time // 60) % 24
minute = temp_time % 60

print(hour, minute)
