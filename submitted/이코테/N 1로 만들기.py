def solution(N, K):
    cnt = 0

    while(N != 1):
        cnt += 1
        if(N % K == 0):
            N = N // K
        else:
            N -= 1

    return cnt

def main():
    N = int(input())
    K = int(input())

    print(solution(N, K))

if (__name__ == "__main__"):
    main()