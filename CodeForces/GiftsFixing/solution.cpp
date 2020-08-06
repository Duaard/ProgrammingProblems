#include <bits/stdc++.h>

using namespace std;

void solve()
{
    int n;
    cin >> n;

    vector<long long> a(n), b(n);
    long long o = INT_MAX, c = INT_MAX;
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
        c = min(c, a[i]);
    }
    for (int i = 0; i < n; i++)
    {
        cin >> b[i];
        o = min(o, b[i]);
    }

    long long ans = 0;
    for (int i = 0; i < n; i++)
    {
        long long candy = a[i] - c;
        long long orange = b[i] - o;

        ans += max(candy, orange);
    }

    cout << ans << "\n";
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