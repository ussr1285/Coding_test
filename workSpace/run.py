def solution(word):
    sec = 0
    for alphabet in word:
        sec += translate(alphabet)
    return sec


def translate(alphabet):
    if alphabet == "1":
        return 2
    elif alphabet == "A" or alphabet == "B" or alphabet == "C":
        return 3
    elif alphabet == "D" or alphabet == "E" or alphabet == "F":
        return 4
    elif alphabet == "G" or alphabet == "H" or alphabet == "I":
        return 5
    elif alphabet == "J" or alphabet == "K" or alphabet == "L":
        return 6
    elif alphabet == "M" or alphabet == "N" or alphabet == "O":
        return 7
    elif alphabet == "P" or alphabet == "Q" or alphabet == "R" or alphabet == "S":
        return 8
    elif alphabet == "T" or alphabet == "U" or alphabet == "V":
        return 9
    elif alphabet == "W" or alphabet == "X" or alphabet == "Y" or alphabet == "Z":
        return 10
    # OPERATOR


if __name__ == "__main__":
    phone_word = input()
    print(solution(phone_word))
