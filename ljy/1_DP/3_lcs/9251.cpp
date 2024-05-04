#include <iostream>
using namespace std;

int cached[1001][1001];
int main()
{
	string fir, sec;
	cin >> fir >> sec;

	for (int i = 1; i <= fir.length(); i++)
	{
		for (int j = 1; j <= sec.length(); j++)
		{
			if (fir[i - 1] == sec[j - 1])
				cached[i][j] = cached[i - 1][j - 1] + 1;

			else cached[i][j] = max(cached[i][j-1], cached[i-1][j]);
		}
	}
	cout << cached[fir.length()][sec.length()];
}