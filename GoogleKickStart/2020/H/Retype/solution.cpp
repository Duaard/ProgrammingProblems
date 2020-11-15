#include <bits/stdc++.h>

using namespace std;

void solve()
{
    int n, k, s;

    cin >> n >> k >> s;

    int ans;

    ans = min(n, (n - s) + (k - s)) + k;

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