def func(S):
    chara = []
    sum_numbers = 0

    for s in S:
        if s.isdecimal():
            sum_numbers += int(s)
        else:
            chara.append(ord(s))

    chara.sort()

    return "".join(map(chr, chara)) + str(sum_numbers)


def main():
    S = input()
    print(func(S))


if __name__ == "__main__":
    main()
