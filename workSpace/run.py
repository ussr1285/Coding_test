def solution(array, commands):
    answer = []

    for command in commands:
        temp_array = array[command[0]-1:command[1]]
        bubble_sort(temp_array) 
        kst_num = temp_array[command[2]-1]
        answer.append(kst_num)
    return answer

def bubble_sort(array):
    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            if(array[i] > array[j]):
                temp = array[i]
                array[i] = array[j]
                array[j] = temp

def main():
    array = [1, 5, 2, 6, 3, 7, 4]
    commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    
    result = solution(array, commands)
    print(result)


if __name__ == "__main__":
    main()

