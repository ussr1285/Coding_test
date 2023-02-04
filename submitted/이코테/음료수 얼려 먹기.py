class Node:
    def __init__(self, data, col, row):
        self.data = data
        self.col = col
        self.row = row
        self.visited = False


def find_zero():
    amount_icecream = 0

    for col in range(N):
        for row in range(M):
            if (not nodes[col][row].visited) and nodes[col][row].data == "0":
                dfs(col, row)
                amount_icecream += 1
            else:
                continue
    return amount_icecream


def dfs(col, row):
    if (not nodes[col][row].visited) and nodes[col][row].data == "0":
        nodes[col][row].visited = True

        if row + 1 < M and row < M:  # right
            dfs(col, row + 1)

        if row > 0:  # left
            dfs(col, row - 1)

        if col > 0 and col < N:  # bottom
            dfs(col - 1, row)

        if col + 1 < N:  # up
            dfs(col + 1, row)
    else:
        return 0


if __name__ == "__main__":
    N, M = list(map(int, input().split(" ")))

    nodes = []
    rows = []

    for col_i in range(N):  # 노드 구성 단계
        row = input()
        rows = []

        for row_i in range(M):
            temp_node = Node(row[row_i], col_i, row_i)
            rows.append(temp_node)
        nodes.append(rows)

    print(find_zero())
