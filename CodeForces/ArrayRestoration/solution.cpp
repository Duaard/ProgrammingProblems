#include <bits/stdc++.h>

using namespace std;

void solve()
{
    int n, x, y;
    cin >> n >> x >> y;

    int dif = y - x;

    int mul = n - 1;
    while (dif % mul != 0)
    {
        mul--;
    }
    mul = dif / mul;
    for (int i = x; i <= y && n > 0; i += mul)
    {
        cout << i << " ";
        n--;
    }

    for (int i = x - mul; i >= 1 && n > 0; i -= mul)
    {
        cout << i << " ";
        n--;
    }

    for (int i = y + mul; n > 0; i += mul)
    {
        cout << i << " ";
        n--;
    }

    cout << "\n";
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