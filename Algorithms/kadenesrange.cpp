#include "./stdc++.h"
using namespace std;

pair<int, int> longestRange(vector<int> nums)
{
    int k = INT_MIN;
    int sum = 0;
    pair<int, int> ans;
    for (int i = 0; i < nums.size(); i++)
    {
        sum += nums[i];
        k = max(sum, k);
        if (sum > k)
        {
            if (sum > 0)
            {
                if (sum == nums[i])
                {
                    // Sum was from 0
                    // Update first and last of ans
                    ans = make_pair(i, i);
                }
                else
                {
                    // Sum had value
                    // Update last of ans
                    ans.second = i;
                }
            }
            else
            {
                // Update ans to i
                ans = make_pair(i, i);
            }
            k = sum;
        }
        sum = max(sum, 0);
    }
    return ans;
}

int main()
{
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++)
    {
        cin >> nums[i];
    }
    pair<int, int> ans = longestRange(nums);
    cout << "{" << ans.first << ", " << ans.second << "}\n";
    return 0;
}