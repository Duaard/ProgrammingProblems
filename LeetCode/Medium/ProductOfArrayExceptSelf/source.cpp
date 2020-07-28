class Solution
{
public:
    vector<int> productExceptSelf(vector<int> &nums)
    {
        const int n = nums.size();

        vector<int> pref_prod;
        pref_prod.push_back(1);
        for (int x : nums)
        {
            pref_prod.push_back(pref_prod.back() * x);
        }

        vector<int> suf_prod(n + 1);
        suf_prod[n] = 1;
        for (int i = n - 1; i > 0; i--)
        {
            suf_prod[i] = suf_prod[i + 1] * nums[i];
        }

        vector<int> ans(n);
        for (int i = 0; i < n; i++)
        {
            ans[i] = pref_prod[i] * suf_prod[i + 1];
        }
        return ans;
    }
};
