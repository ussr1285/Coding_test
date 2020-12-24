#include <iostream>
#include <string>
using namespace std;

#define MAX 32 //9

int main()
{
    int A = 0;
    int B = 0;
    int quotient;
    int remainder;
    int decimalPoint = 0;
    string result = "";

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
            result.append(to_string(quotient));
            break;
        }
        else
        {
            if (decimalPoint == 0)
            {
                //cout << "result: " << result << "\n";
                result.append("0.");
                A = A * 10;
                continue;
            }

            result.append(to_string(quotient));
            //cout << "result: " << result << "\n";
            A = remainder * 10;
        }

    } while (decimalPoint++ < MAX);

    cout << result;

    return 0;
}
