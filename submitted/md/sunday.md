

# 백준 3052

## 문제

두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지 이다. 예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2이다. 

수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.

## 입력

첫째 줄부터 열번째 줄 까지 숫자가 한 줄에 하나씩 주어진다. 이 숫자는 1,000보다 작거나 같고, 음이 아닌 정수이다.

## 출력

첫째 줄에, 42로 나누었을 때, 서로 다른 나머지가 몇 개 있는지 출력한다.

## 예제 입력 1

```
1
2
3
4
5
6
7
8
9
10
```

## 예제 출력 1

```
10
```

각 수를 42로 나눈 나머지는 1, 2, 3, 4, 5, 6, 7, 8, 9, 10이다.



- 코드

```python
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
    

```



# 백준 1546

## 문제

세준이는 기말고사를 망쳤다. 세준이는 점수를 조작해서 집에 가져가기로 했다. 일단 세준이는 자기 점수 중에 최댓값을 골랐다. 이 값을 M이라고 한다. 그리고 나서 모든 점수를 점수/M*100으로 고쳤다.

예를 들어, 세준이의 최고점이 70이고, 수학점수가 50이었으면 수학점수는 50/70*100이 되어 71.43점이 된다.

세준이의 성적을 위의 방법대로 새로 계산했을 때, 새로운 평균을 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 시험 본 과목의 개수 N이 주어진다. 이 값은 1000보다 작거나 같다. 둘째 줄에 세준이의 현재 성적이 주어진다. 이 값은 100보다 작거나 같은 음이 아닌 정수이고, 적어도 하나의 값은 0보다 크다.

## 출력

첫째 줄에 새로운 평균을 출력한다. 실제 정답과 출력값의 절대오차 또는 상대오차가 10-2 이하이면 정답이다.

## 예제 입력 1

```
3
40 80 60
```

## 예제 출력 1

```
75.0
```

- 코드

```python
def solution(N, score):
    new_score = []
    M = max(score)
    for i in range(N):
        new_score.append(score[i]/M*100)
        
    return sum(new_score)/len(new_score)

def main():
    N = int(input())
    score = input().split(" ")
    score = list(map(int, score))
    
    print(round(solution(N, score), 6))

if(__name__ == "__main__"):
    main()
```



