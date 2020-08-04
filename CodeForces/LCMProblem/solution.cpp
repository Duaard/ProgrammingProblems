#include <bits/stdc++.h>

using namespace std;

void solve()
{
    long long l, r;

    cin >> l >> r;

    if (2l > r)
    {
        cout << "-1 -1\n";
    }
    else
    {
        cout << l << " " << 2l << "\n";
    }
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