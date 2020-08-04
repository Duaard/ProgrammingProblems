#include <bits/stdc++.h>

using namespace std;

void solve()
{
    long long l, r;

    cin >> l >> r;

    while (true)
    {
        if (r % l == 0)
        {
            cout << l << " " << r << "\n";
            break;
        }
        else
        {
            r -= r % l;
        }

        if (r <= l)
        {
            cout << "-1 -1\n";
            break;
        }
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