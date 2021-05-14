##
# 이 프로그램은 주급을 계산한다.
#
def weeklyPay(rate, hour):
    weekMoney = 0
    
    # if else를 이용한 주급 계산.
    if(hour > 30):
        weekMoney += rate * 30
        rate *= 1.5
        weekMoney += rate * (hour - 30)
    else:
        weekMoney += rate * hour

    return weekMoney

rate = int(input("시급을 입력하시오:"))
hour = int(input("근무 시간을 입력하시오:"))
print("주급은 " + str(weeklyPay(rate, hour)))
