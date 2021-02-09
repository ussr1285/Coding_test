def minimum_escape_maze():  # Use N, M, maze
    cnt = 0

    for _ in range(N):
        visited.append([False for _ in range(M)])

    ident_seq = deque([[0, 0]])  # bfs

    while ident_seq:
        i_j = ident_seq.popleft()
        i, j = i_j
        possible_way = [False, False, False, False]

        cnt += 1

        if i == N and j == M:
            break

        # print(i_j, "boolean test:")

        # analysis
        if is_possible(i + 1, j):  # up
            possible_way[0] = True
        if is_possible(i - 1, j):  # down
            possible_way[1] = True
        if is_possible(i, j + 1):  # right
            possible_way[2] = True
        if is_possible(i, j - 1):  # left
            possible_way[3] = True

        # go
        move_direction = [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]
        if sum(possible_way) == 1:
            if possible_way[0]:  # up
                ident_seq.append(move_direction[0])
            if possible_way[1]:  # down
                ident_seq.append(move_direction[1])
            if possible_way[2]:  # right
                ident_seq.append(move_direction[2])
            if possible_way[3]:  # left
                ident_seq.append(move_direction[3])
        else:  # BFS 로 구현해야 할 듯..
            distance = []

            for _i in range(len(move_direction)):
                if possible_way[_i]:
                    caculated_distance = move_direction[_i][0] + move_direction[_i][1]
                    distance.append(caculated_distance)
            print("min:", distance.index(min(distance)))

        visited[i][j] = True
        print("----")  # test
        for temp in visited:
            print(temp)

    return cnt


def is_possible(i, j):
    bool_result = (
        i >= 0
        and i < N
        and j >= 0
        and j < M
        and (not visited[i][j])
        and maze[i][j] == "1"
    )

    return bool_result


if __name__ == "__main__":
    from collections import deque

    N, M = list(map(int, input().split(" ")))
    maze = []
    visited = []

    for _ in range(N):
        maze.append(input())

    print(minimum_escape_maze())
