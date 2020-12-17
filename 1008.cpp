#include<iostream>

int divideFunc(int howMany, int A, int B) {
	using namespace std;

	if (howMany == 2) {
		cout << ".";
	}

	if (howMany > 10) {
		return 0;
	}

	int AdivB = A / B;
	int AremainB = A % B;

	if (AremainB == 0) {
		cout << AdivB;
		return 0;
	}
	else {
		cout << AdivB;
		return divideFunc(++howMany, A*10, B);
	}

}

int main() {
	using namespace std;

	int A = 0;
	int B = 0;

	cin >> A;
	cin >> B;

	divideFunc(1, A, B);


	return 0;
}