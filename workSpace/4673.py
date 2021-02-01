def d(n):
    str_n = str(n)

    for each_num in str_n:
        n += int(each_num)
    return n


def repeat_1to10000():
    for n in range(1, 10001):
        dn = d(n)
        d_list.append(dn)

    for i in range(1, 10001):
        if i in d_list:
            continue
        else:
            print(i)


def main():
    repeat_1to10000()


if __name__ == "__main__":
    d_list = []
    main()