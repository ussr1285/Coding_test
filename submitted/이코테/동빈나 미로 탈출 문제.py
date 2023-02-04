def minimum_escape_maze():  # Use N, M, maze
    cnt = 0

    for _ in range(N):
        visited.append([False for _ in range(M)])

    ident_seq = deque([[0, 0]])  # bfs

    while ident_seq:
        i_j = ident_seq.pop()
        i, j = i_j
        possible_way = [False, False, False, False]

        cnt += 1

        if is_possible(i - 1, j):  # down
            possible_way[0] = True
        if is_possible(i, j + 1):  # right
            possible_way[1] = True
        if is_possible(i, j - 1):  # left
            possible_way[2] = True
        if is_possible(i + 1, j):  # up
            possible_way[3] = True

        # go
        move_direction = [[i - 1, j], [i, j + 1], [i, j - 1], [i + 1, j]]
        for _i in range(len(move_direction)):
            if possible_way[_i]:
                maze[move_direction[_i][0]][move_direction[_i][1]] = maze[i][j] + 1
                ident_seq.append(move_direction[_i])

        visited[i][j] = True

    return maze[N - 1][M - 1]


def is_possible(i, j):
    bool_result = (
        i >= 0
        and i < N
        and j >= 0
        and j < M
        and (not visited[i][j])
        and maze[i][j] == 1
    )
    return bool_result


if __name__ == "__main__":
    from collections import deque

    N, M = list(map(int, input().split(" ")))
    maze = []
    visited = []

    for _ in range(N):
        maze.append(list(map(int, input())))

    print(minimum_escape_maze())
