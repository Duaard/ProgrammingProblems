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

    int mx = INT_MIN, ans = 0;

    for (int i = 0; i < n; i++)
    {
        if (nums[i] > mx && (i == n - 1 || nums[i + 1] < nums[i]))
            ans++;
        mx = max(mx, nums[i]);
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