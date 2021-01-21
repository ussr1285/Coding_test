#include <iostream>
using namespace std;

int main()
{
    int arr[9] = {0};
    int max = 0;
    int max_index = -1;

    for(int i = 0; i < 9; i++){
        cin >> arr[i];
        if(max < arr[i]){
            max = arr[i]; 
            max_index = i + 1;
        }
    }

    cout << max << "\n" << max_index;

    return 0;
}
