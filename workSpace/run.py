# from collections import deque
"""
class Node:
    def __init__(self, data, row_i, col_i):
        self.data = data
        self.row_i = row_i
        self.col_i = col_i
"""


def available_amount_icecream(rows):
    amount_icecream = 0

    return amount_icecream


def main():
    input_NM = input().split(" ")
    N = int(input_NM[0])  # amount of columns
    M = int(input_NM[1])  # amount of rows

    rows = []

    for _ in range(N):
        row = input()
        row = row[0:M]
        rows.append(row)


if __name__ == "__main__":
    main()
