def a(n):
    return sum(n)


def main():
    n = list(map(int, input().split(" ")))
    print(a(n))


if __name__ == "__main__":
    main()
