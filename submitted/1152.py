def count_word(string):
    string = string.strip()
    string = string.replace("  ", " ")
    string = string.split(" ")

    # print("---", string, "---") # 문자열이 어떻게 나오지는지 확인

    if len(string) == 1 and string[0] == "":
        length_of_string = 0
    else:
        length_of_string = len(string)
    return length_of_string


if __name__ == "__main__":
    string = input()
    print(count_word(string))
