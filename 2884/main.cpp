#include<iostream>
using namespace std;

#define HMAX = 24;
#define MMAX = 60;

int main(){
    int H = 0;
    int M = 0;

    cin >> H;
    cin >> M;

    M -= 45;

    if( M < 0 ){
        H -= 1;
        M += 60;
    }

    if( H < 0 ){
        H += 24;
    }

    cout << H << " " << M;
    

    return 0;
}