#include <iostream>
using namespace std;

int main(){
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);

    int T = 0;

    cin >> T;

    int *A = new int[T];
    int *B = new int[T];


    for(int i=0; i<T; i++){
        cin >> A[i];
        cin >> B[i];
        cout << A[i] + B[i] << "\n";
    }


    return 0;
}
