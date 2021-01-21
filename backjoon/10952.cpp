#include <iostream>
using namespace std;

int main()
{
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);

    int A;
    int B;

    while (true)
    {
        cin >> A;
        cin >> B;

        if(A == 0 && B == 0){
            break;
        }

        cout << A + B << "\n";
    }
    

    return 0;
}

