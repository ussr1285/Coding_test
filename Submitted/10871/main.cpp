#include <iostream>
using namespace std;

int main()
{
    int N = 0;
    int X = 0;
    int *arr;

    cin >> N;
    cin >> X;

    arr = new int[N];

    for (int i = 0; i < N; i++)
    {
        cin >> arr[i];
    }

    for (int i = 0; i < N; i++)
    {
        if(arr[i] < X){
            cout << arr[i] << " ";
        }
    }

    return 0;
}
