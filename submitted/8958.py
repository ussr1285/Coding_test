def solution(N, list_ox):
    score_list = [0] * len(list_ox)
    
    temp_score = 0
    

    for i in range(N):
        temp_score = 0
        for j in range(len(list_ox[i])):
            if((list_ox[i])[j] == 'O'):
                temp_score += 1
            else:
                temp_score = 0
            score_list[i] += temp_score

    return score_list


def main():
    N = int(input())
    list_ox = []

    for i in range(N):
        list_ox.append(input())

    result = solution(N, list_ox)

    for i in range(len(result)):
        print(result[i])
    

if (__name__ == "__main__"):
    main()
