class Node:
    def __init__(self, data, col, row):
        self.data = data
        self.col = col
        self.row = row
        self.visited = False


def find_zero(nodes):
    amount_icecream = 0

    for col in range(len(nodes)):
        for row in range(len(nodes[col])):
            dfs(nodes, col, row)

    return amount_icecream


def dfs(nodes, col, row):
    N = len(nodes)
    M = len(nodes[col])

    if nodes[col][row].visited or nodes[col][row] == 1:
        return 0
    else:
        if col >= N or row >= M:
            return 0
        nodes[col][row].visited = True
        if col > 0:  # bottom
            dfs(nodes, col - 1, row)
        if col + 1 < N:  # up
            dfs(nodes, col + 1, row)
        if row > 0:  # left
            dfs(nodes, col, row - 1)
        if row + 1 < M:  # right
            dfs(nodes, col, row + 1)
        print(col, row)


def main():
    input_NM = input().split(" ")
    N = int(input_NM[0])  # length of columns
    M = int(input_NM[1])  # length of rows

    rows = []

    for col_i in range(N):  # 노드 구성 단계
        row = input()
        rows = []

        for row_i in range(M):
            temp_node = Node(row[row_i], col_i, row_i)
            rows.append(temp_node)
        nodes.append(rows)

    find_zero(nodes)


if __name__ == "__main__":
    # from collections import deque
    nodes = []
    main()