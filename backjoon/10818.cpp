#include <iostream>
using namespace std;

int main()
{
    int N = 0;
    int min = 0;
    int max = 0;
    int temp = 0;

    cin >> N;

    int *arr = new int[N];

    for (int i = 0; i < N; i++)
    {
        cin >> arr[i];
    }

    min = arr[0];
    max = arr[0];

    // 단순 비교
    for (int i = 1; i < N; i++){
        if(arr[i] > max){
            max = arr[i];
        }
        if(arr[i] < min){
            min = arr[i];
        }
    }



    cout << min << " " << max;
}
