#include<iostream>

using namespace std;

int func(int N, int cnt){
	int temp = N-(6*cnt);
	if (N <=1){
		return cnt;
	}
	else{
		return func(temp, cnt + 1);
	}
}

int main(){
	int N;
	cin >> N; 
	cout << func(N, 1);
	return 0;
}

/*

'''
1 : 1 : 1
2~7 : 6 : 2
8~19 : 12 : 3
20~37 : 18 : 4
38~61 : 24 : 5
.
.
.

Sigma(6,K) : 6*(N-1) : N




'''

*/