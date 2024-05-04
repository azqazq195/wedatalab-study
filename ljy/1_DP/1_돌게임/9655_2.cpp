#include <iostream>
#include <cstring>

using namespace std;

int cached[1001];

int main()
{
	int n;

	cin >> n;

	for (int i = 1; i <= n; i++)
	{
		if (i < 3)
			cached[i] = i;
		else cached[i] = cached[i - 2];
	}
	if (cached[n] % 2 == 1)
		cout << "SK";
	else cout << "CY";
}