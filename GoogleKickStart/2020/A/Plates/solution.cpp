#include <bits/stdc++.h>

using namespace std;

void solve()
{
    int n, k, p;
    cin >> n >> k >> p;

    vector<vector<int>> plates(n, vector<int>(k));

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < k; j++)
        {
            cin >> plates[i][j];
            // printf("plates[%i][%i]: %i\n", i, j, plates[i][j]);
        }
    }

    // Create sums
    vector<vector<int>> sums(n + 1, vector<int>(p + 1));

    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= p; j++)
        {
            int val = 0;
            if (j <= k)
            {
                val = plates[i - 1][j - 1];
                // cout << "val: " << val << " j: " << j << "\n";
            }
            sums[i][j] = sums[i][j - 1] + val;
            // printf("sums[%i][%i]: %i\n", i, j, sums[i][j]);
        }
    }

    // Calculate dp
    vector<vector<int>> dp(n + 1, vector<int>(p + 1));

    for (int i = 1; i <= n; i++)
    {
        for (int j = 0; j <= p; j++)
        {
            // Loop through all possible x
            dp[i][j] = 0;
            for (int x = 0; x <= j; x++)
            {
                dp[i][j] = max(dp[i][j], dp[i - 1][j - x] + sums[i][x]);
            }
        }
    }

    cout << dp[n][p] << "\n";
    // for (int i = 0; i <= n; i++)
    // {
    //     for (int j = 0; j <= p; j++)
    //     {
    //         printf("dp[%i][%i]: %i\n", i, j, dp[i][j]);
    //     }
    // }
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