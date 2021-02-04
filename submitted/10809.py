if __name__ == "__main__":
    S = input()
    alphabets = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]

for alphabet in alphabets:
    if alphabet in S:
        print(S.index(alphabet), end=" ")
    else:
        print(-1, end=" ")
