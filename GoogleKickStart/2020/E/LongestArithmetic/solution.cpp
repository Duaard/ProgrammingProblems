#include <bits/stdc++.h>

using namespace std;

void solve()
{
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++)
    {
        cin >> nums[i];
    }
    int ans = 0, prev = nums[0], diff = 0, cur = 1;
    bool no_diff = true;

    for (int i = 1; i < n; i++)
    {
        if (no_diff || nums[i] - prev == diff)
        {
            cur++;
            no_diff = false;
        }
        else
        {
            cur = 2;
        }
        ans = max(ans, cur);
        diff = nums[i] - prev;
        prev = nums[i];
    }
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