#include <bits/stdc++.h>

using namespace std;

void solve()
{
	int n, m;
	cin >> n >> m;
	vector<int> a(n);
	vector<int> b(m);
	for (int i = 0; i < n; i++)
	{
		cin >> a[i];
	}
	for (int i = 0; i < m; i++)
	{
		cin >> b[i];
	}

	unordered_map<int, int> pairs;
	bool flag = false;
	for (int x : a)
	{
		pairs[x]++;
	}
	for (int x : b)
	{
		if (pairs[x])
		{
			cout << "YES\n";
			cout << "1 " << x << "\n";
			flag = true;
			break;
		}
	}
	if (!flag)
		cout << "NO\n";
}

int main()
{
	int t;
	cin >> t;
	while (t--)
	{
		solve();
	}
}