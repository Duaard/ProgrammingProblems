#include <bits/stdc++.h>

using namespace std;

void solve()
{
    int x, y, z;
    cin >> x >> y >> z;

    if (x == max(y, z) || y == max(x, z) || z == max(x, y))
    {
        cout << "YES\n";
        cout << min(x, y) << " " << min(x, z) << " " << min(y, z) << "\n";
    }
    else
    {
        cout << "NO\n";
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