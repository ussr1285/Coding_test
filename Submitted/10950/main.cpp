#include <iostream>
using namespace std;

int main()
{
    int length = 0;

    cin >> length;

    int *A = new int[length];
    int *B = new int[length];

    for (int i = 0; i < length; i++)
    {
        cin >> A[i];
        cin >> B[i];
        
    }

    for (int i = 0; i < length; i++)
    {
        cout << A[i] + B[i] << "\n";
    }


    return 0;
}