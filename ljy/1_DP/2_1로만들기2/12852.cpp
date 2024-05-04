#include<iostream>
#include<cstring>
#include<vector>

using namespace std;

int cached[1000001];
int result[1000001];

int make_one(int n)
{
	if (n == 1)
		return 0;

	if (cached[n] != -1) 
		return cached[n];

	cached[n] = make_one(n - 1) + 1;
	result[n] = n - 1;
	if (n % 2 == 0)
	{
		int temp = make_one(n / 2) + 1;
		if (cached[n] > temp)
		{
			cached[n] = temp;
			result[n] = n / 2;
		}
	}

	if (n % 3 == 0)
	{
		int temp = make_one(n / 3) + 1;
		if (cached[n] > temp)
		{
			cached[n] = temp;
			result[n] = n / 3;
		}
	}

	return cached[n];
}

int main()
{
	memset(cached, -1, sizeof(cached));

	int n;
	cin >> n;
	cout << make_one(n) << endl;

	while (result[n] != 0)
	{
		cout << n << " ";
		n = result[n];
	}
	cout << '1' << endl;
}