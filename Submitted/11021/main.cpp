#include <iostream>
using namespace std;

int main(){
    int T = 0;
    int *A;
    int *B;

    cin >> T;

    A = new int[T];
    B = new int[T];

    for(int i=0; i<T; i++){
        cin >> A[i];
        cin >> B[i];
    }

    for(int i=0; i<T; i++){
        cout << "Case #" << i+1 << ": " << A[i] + B[i] << "\n";
    }

    return 0;
}
