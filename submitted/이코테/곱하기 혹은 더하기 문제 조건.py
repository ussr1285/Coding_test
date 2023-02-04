def solution(S):
    result = int(S[0])

    for i in range(1, len(S)):
        number = int(S[i])

        if(number == 0 or number == 1 or result == 0 or result == 1):
            result += number
        else:
            result *= number
    
    return result


def main():
    S = input()
    print(solution(S))
    

if (__name__ == "__main__"):
    main()