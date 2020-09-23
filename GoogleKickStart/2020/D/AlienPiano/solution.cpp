#include <bits/stdc++.h>

using namespace std;

int getDiff(int a, int b)
{
    if (a > b)
    {
        return -1;
    }
    else if (b < a)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

void solve()
{
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++)
    {
        cin >> nums[i];
    }

    int ans = 0;
    vector<vector<int>> dp(n, vector<int>(4));
    for (int i = 1; i < n; i++)
    {
        int pitch = nums[i];
        int prev = nums[i - 1];
        int diff = getDiff(pitch, prev);
        for (int j = 0; j < 4; j++)
        {
            dp[i][j] = INT_MAX;
            for (int k = 0; k < 4; k++)
            {

                dp[i][j] = min(dp[i][j], dp[i - 1][k]
            }
        }
    }
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