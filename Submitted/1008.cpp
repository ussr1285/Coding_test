#include <iostream>
using namespace std;

#define MAX 32 //9

int main()
{
    double A = 0;
    double B = 0;

    cin >> A;
    cin >> B;

    cout.precision(MAX);
    cout << A / B;

    return 0;
}
