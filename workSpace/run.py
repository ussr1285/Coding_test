def repeat(r, s):
    string_arr = []
    for word in s:
        for _ in range(r):
            string_arr.append(word)

    string = "".join(string_arr)

    return string


if __name__ == "__main__":
    T = int(input())
    R = []
    S = []

    for _ in range(T):
        r, s = input().split(" ")
        R.append(int(r))
        S.append(s)

    for i in range(T):
        print(repeat(R[i], S[i]))
