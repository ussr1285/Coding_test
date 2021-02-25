def bin_find_x(nums, X):
    start = 0
    end = len(nums) - 1

    while start < end:
        mid = (start + end) // 2

        if not (X in nums[start:end]):
            break
        if nums[mid] > X:
            end = mid
        elif nums[mid] < X:
            start = mid
        elif nums[mid] == X:
            return mid

    return -1


def x_amount(nums, X):
    x_location = bin_find_x(nums, X)
    cnt = 1
    left = x_location - 1
    right = x_location + 1

    if x_location != -1:
        while nums[left] == X:
            cnt += 1
            left -= 1
        while nums[right] == X:
            cnt += 1
            right += 1
        return cnt
    else:
        return x_location


if __name__ == "__main__":
    N, X = list(map(int, input().split(" ")))
    nums = list(map(int, input().split(" ")))[0:N]
    print(x_amount(nums, X))
