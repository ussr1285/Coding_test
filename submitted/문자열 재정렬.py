def func(S):
    chara = []
    numbers = []

    for s in S:
        if s.isdecimal():
            numbers.append(int(s))
        else:
            chara.append(ord(s))

    numbers.sort()
    chara.sort()

    return "".join(map(chr, chara)) + "".join(list(map(str, numbers)))


def main():
    S = input()
    print(func(S))


if __name__ == "__main__":
    main()
