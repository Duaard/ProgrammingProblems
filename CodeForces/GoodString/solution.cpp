#include <bits/stdc++.h>

using namespace std;

int getAns(const string &s, int x, int y)
{
    int ans = 0;
    for (auto c : s)
    {
        if (c - '0' == x)
        {
            ans++;
            swap(x, y);
        }
    }

    if (x != y && ans % 2 != 0)
    {
        ans--;
    }
    return ans;
}

void solve()
{
    string s;
    cin >> s;

    const int n = s.size();

    int ans = 0;
    for (int x = 0; x < 10; x++)
    {
        for (int y = 0; y < 10; y++)
        {
            ans = max(ans, getAns(s, x, y));
        }
    }

    cout << n - ans << "\n";
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