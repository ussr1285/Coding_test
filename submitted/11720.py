def sum_fucntion(arr, i, N):
    if i > N - 1:
        return 0
    return int(arr[i]) + sum_fucntion(arr, i + 1, N)


def main():
    N = int(input())
    arr = input()

    print(sum_fucntion(arr, 0, N))


if __name__ == "__main__":
    main()
