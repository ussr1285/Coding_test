def make_max_arr(A, B, K):
    A = quick_sort(A)
    B = quick_sort(B)

    for i in range(K):
        if A[i] > B[-i - 1]:
            break

        A[i], B[-i - 1] = B[-i - 1], A[i]

    return sum(A)


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]

    left = [arr[i] for i in range(1, len(arr)) if arr[i] <= pivot]
    right = [arr[i] for i in range(1, len(arr)) if arr[i] > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


if __name__ == "__main__":
    N, K = list(map(int, input().split(" ")))
    A = list(map(int, input().split(" ")))[0:N]
    B = list(map(int, input().split(" ")))[0:N]

    print(make_max_arr(A, B, K))
