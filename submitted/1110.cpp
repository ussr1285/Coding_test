#include <iostream>
using namespace std;

int main()
{
    int N = 0;
    int cnt = 0;
    int tens = 0;
    int units = 0;
    int temptens = 0;
    int tempunits = 0;
    int temp = 0;

    cin >> N;

    if (N < 10)
    {
        tens = 0;  
    }else{
        tens = N / 10;
    }
    units = N % 10;

    temptens = tens;
    tempunits = units;

    while (true)
    {
        cnt++;
        temp = tempunits;
        tempunits = (temptens + tempunits) % 10;
        temptens = temp;

        if (temptens == tens && tempunits == units)
        {
            break;
        }
    }

    cout << cnt;

    return 0;
} 