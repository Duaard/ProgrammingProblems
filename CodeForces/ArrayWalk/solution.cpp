#include <bits/stdc++.h>

using namespace std;

void solve()
{
    int n, k, z;
    cin >> n >> k >> z;
    vector<int> nums(n);
    for (int i = 0; i < n; i++)
    {
        cin >> nums[i];
    }

    int ans = 0, s, p;
    for (int t = 0; t < z + 1; t++)
    {
        int pos = k - 2 * t;
        if (pos < 0)
        {
            continue;
        }
        s = 0;
        p = 0;
        for (int i = 0; i < pos + 1; i++)
        {
            if (i < n - 1)
            {
                p = max(p, nums[i] + nums[i + 1]);
            }
            s += nums[i];
        }
        ans = max(ans, s + p * t);
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