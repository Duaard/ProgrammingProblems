#include <bits/stdc++.h>

using namespace std;

void solve()
{
    int n;
    long long d;

    cin >> n >> d;

    vector<long long> trips(n);

    for (int i = 0; i < n; i++)
    {
        cin >> trips[i];
    }

    long long mod;
    for (int i = n - 1; i >= 0; i--)
    {
        mod = d % trips[i];
        d -= mod;
    }

    cout << d << "\n";
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