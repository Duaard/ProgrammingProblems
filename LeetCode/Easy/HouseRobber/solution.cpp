class Solution
{
public:
    int rob(vector<int> &nums)
    {
        const int n = nums.size();
        if (!n)
        {
            return 0;
        }
        vector<int> dp(n);

        for (int i = 0; i < n; i++)
        {
            int less2 = 0, less3 = 0;
            int last_val = 0;
            if (i - 2 >= 0)
            {
                less2 += dp[i - 2];
            }
            if (i - 3 >= 0)
            {
                less3 += dp[i - 3];
            }
            if (i)
            {
                last_val = dp[i - 1];
            }

            dp[i] = max(less2, less3);
            dp[i] = max(last_val, dp[i] + nums[i]);
        }

        return dp[n - 1];
    }
};