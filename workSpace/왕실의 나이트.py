col_index = ["a", "b", "c", "d", "e", "f", "g", "h"]


def func(input_str):
    cnt = 0
    col = input_str[0]
    row = int(input_str[1])

    # above
    if col_index.index(col) + 2 < len(col_index):
        if row - 1 > 0:  # left
            cnt += 1
        if row + 1 < 9:  # right
            cnt += 1
    # right
    if row + 2 < 9:
        if col_index.index(col) + 1 < len(col_index):  # above
            cnt += 1
        if col_index.index(col) - 1 > len(col_index):  # below
            cnt += 1
    # left
    if row - 2 > 0:
        if col_index.index(col) + 1 < len(col_index):  # above
            cnt += 1
        if col_index.index(col) - 1 > len(col_index):  # below
            cnt += 1
    # below
    if col_index.index(col) - 2 >= 0:
        if row - 1 > 0:  # left
            cnt += 1
        if row + 1 < 9:  # right
            cnt += 1

    return cnt


def main():
    input_str = input()

    print(func(input_str))


if __name__ == "__main__":

    main()
