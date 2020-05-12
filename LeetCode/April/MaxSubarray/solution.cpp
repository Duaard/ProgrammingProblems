class Solution
{
public:
    int maxSubArray(vector<int> &nums)
    {
        int ans = INT_MIN, sub = 0;
        for (int x : nums)
        {
            sub += x;
            ans = max(ans, sub);
            sub = max(sub, 0);
        }

        return ans;
    }
};