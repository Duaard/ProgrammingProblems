#include <bits/stdc++.h>

using namespace std;

void solve()
{
    int n, x;
    cin >> n >> x;

    if (n <= 2)
    {
        cout << "1\n";
        return;
    }

    int ans = (n - 3) / x;
    cout << ans + 2 << "\n";
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