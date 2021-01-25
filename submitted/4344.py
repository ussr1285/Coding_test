def solution(N, score):
    over_mean_ratio = []
    i = 0

    for each_score in score:
        #print("----", sum(each_score), N[i], "----")
        mean = sum(each_score) / N[i]
        over_mean_cnt = 0

        for j in range(len(each_score)):
            if(each_score[j] > mean):
                over_mean_cnt += 1

        over_mean_per = round(over_mean_cnt / N[i] * 100, 3)
        over_mean_ratio.append(over_mean_per)
        i += 1
        
    return over_mean_ratio

def main():
    C = int(input())
    N = []
    score = []

    for i in range(C):
        user_input = input()
        user_input = user_input.split(' ')
        N.append(int(user_input.pop(0)))
        input_score = list(map(int, user_input))
        score.append(input_score)


    result_list = solution(N, score)

    for result in result_list:
        print(format(result, ".3f"), "%", sep='')

if(__name__ == "__main__"):
    main()
