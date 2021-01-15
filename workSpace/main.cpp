#include <iostream>
using namespace std;

int main()
{
    int inputArr[3] = {0};
    int total = 1;
    int unit = 1;
    int divided = 0;
    int n = 0;
    int cntUnit[10] = {0};

    for (int i = 0; i < 3; i++)
    {
        cin >> inputArr[i];
        total *= inputArr[i];
    }
    cout << "I am total : " << total << "\n";

    while (true)
    {
        divided = total / unit;
        if (divided == 0)
        {
            unit /= 10;
            n--;
            break;
        }
        unit *= 10;
        n++;
    }

    for (int i = 0; i <= n; i++)
    {
        if(i == 0){
            divided = total / unit;
            cout << "I'm 1st: " << divided << "\n";
        }
        else{
            divided = (total % (unit*10)) / unit;
            cout << "I'm " << i+1 << "st , " << divided << " \n";
        }
        
        cntUnit[divided] += 1;
        unit /= 10;
    }

    for(int i = 0; i <= 9; i++){
        cout << cntUnit[i] << "\n";
    }

    return 0;
}
