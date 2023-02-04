def bin_exploer_bread_height(breads, M, start, end):
    mid = (start + end) // 2  # height of bread

    rest_bread = 0

    for bread in breads:
        if bread > mid:
            rest_bread += bread - mid

    if M > rest_bread:
        end = mid
    elif M < rest_bread:
        start = mid
    else:
        return mid

    return bin_exploer_bread_height(breads, M, start, end)


def max_bread_cut(breads, M):
    breads.sort()
    """
    # 선형 탐색 떡 자르기 (떡 길이 기준치 안되는 떡도 전부 자름)
    height_bread = 0
    while True:
        rest_bread = 0
        height_bread -= 1

        for bread in breads:
            if bread > height_bread:
                rest_bread += bread - height_bread
        print("rest_bread:", rest_bread)
        if rest_bread >= M:
            break
        """

    height_bread = bin_exploer_bread_height(breads, M, 0, breads[-1])

    return height_bread


if __name__ == "__main__":
    N, M = list(map(int, input().split(" ")))
    breads = list(map(int, input().split(" ")))[0:N]

    print(max_bread_cut(breads, M))
