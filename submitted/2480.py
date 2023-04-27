dice = list(map(int, input().split(" ")))

price = 0

if(dice[0] == dice[1] == dice[2]):
    price = 10000+dice[0]*1000
else:
    same_two_dice = False
    same_thing = 0

    if(dice[0] == dice[1]):
        same_two_dice = True
        same_thing = dice[0]
    elif(dice[1] == dice[2]):
        same_two_dice = True
        same_thing = dice[1]
    elif(dice[0] == dice[2]):
        same_two_dice = True
        same_thing = dice[2]
    else:
        price = max(dice)*100

    if(same_two_dice):
        price = 1000+same_thing*100

print(price)