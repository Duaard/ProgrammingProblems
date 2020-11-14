#include <bits/stdc++.h>

using namespace std;

void solve()
{
    int n;
    cin >> n;

    vector<vector<long long>> m(n, vector<long long>(n));

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cin >> m[i][j];
            int sub = min(i, j);
            if (i != 0 && j != 0)
            {
                m[i - sub][j - sub] += m[i][j];
            }
        }
    }

    long long ans = 0;

    for (int i = 0; i < n; i++)
    {
        ans = max(ans, m[0][i]);
        ans = max(ans, m[i][0]);
    }

    cout << ans << "\n";
}

int main()
{
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++)
    {
        cout << "Case #" << i << ": ";
        solve();
    }
}