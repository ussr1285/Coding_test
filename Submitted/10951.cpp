#include <iostream>
using namespace std;

int main()
{
    int A;
    int B;

    while (true)
    {
        cin >> A;
        cin >> B;
        if (cin.eof())
        {
            break;
        }
        cout << A + B << "\n";
    }

    return 0;
}