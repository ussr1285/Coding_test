def solution(N, score):

    new_score = []

    M = max(score)

    for i in range(N):
        new_score.append(score[i]/M*100)
        
    return sum(new_score)/len(new_score)

def main():
    N = int(input())
    score = input().split(" ")
    score = list(map(int, score))
    
    print(round(solution(N, score), 6))

if(__name__ == "__main__"):
    main()