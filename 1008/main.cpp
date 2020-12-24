#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    int A = 0;
    int B = 0;
    int quotient;
    int remainder;
    int decimalPoint = 0;
    float result = 0;

    cin >> A;
    cin >> B;

    do
    {
        //cout << "----- " << decimalPoint << " -----\n";
        //cout << A << " vs " << B << "\n";
        quotient = A / B;
        remainder = A % B;

        if (remainder == 0)
        {
            result += quotient * pow(10, -decimalPoint);
            break;
        }
        else
        {
            if (decimalPoint == 0)
            {
                //cout << "result: " << result << "\n";
                A = A * 10;
                continue;
            }

            result += quotient * pow(10, -decimalPoint);
            cout << "result: " << result << "\n";
            A = remainder * 10;
        }

    } while (decimalPoint++ < 9);

    cout << result;

    return 0;
}
