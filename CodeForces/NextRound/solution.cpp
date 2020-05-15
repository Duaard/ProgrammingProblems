#include <bits/stdc++.h>
using namespace std;

int nextRound(vector<int> nums, int k)
{
    int n = nums.size();
    int ans = 0;
    int m = INT_MIN;
    for (int i = 0; i < n; i++)
    {
        if (i == k)
        {
            m = nums[k];
        }
        if (nums[i] >= m && nums[i] > 0)
        {
            ans++;
        }
    }

    return ans;
}

int main()
{
    int n, k;
    cin >> n >> k;
    vector<int> nums;
    int num;
    for (int i = 0; i < n; i++)
    {
        cin >> num;
        nums.push_back(num);
    }
    cout << nextRound(nums, k - 1);
    return 0;
}