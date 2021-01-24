def solution():
    list_input = []
    exist_list = []

    for i in range(10):
        list_input.append(int(input()) % 42)

    for i in range(10):
        if(list_input[i] in exist_list):
            continue
        else:
            exist_list.append(list_input[i])
            
    return len(exist_list)

def main():
    result = solution()
    print(result)

if __name__ == "__main__":
    main()
    
