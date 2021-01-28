def solution(X_list):
    maximum_group = 0
    i = 0
    cnt = 0

    X_list.sort()

    for i in range(len(X_list)):
        cnt += 1
        if X_list[i] <= cnt:
            maximum_group += 1
            cnt = 0

    return maximum_group


def main():
    X_list = list(map(int, input().split(" ")))
    print(solution(X_list))


if __name__ == "__main__":
    main()
