#include <bits/stdc++.h>
using namespace std;

int f(int n, vector<int> &nums)
{
    sort(nums.begin(), nums.end());
    int l = INT_MAX;
    for (int i = 0; i < n - 1; i++)
    {
        l = min(abs(nums[i] - nums[i + 1]), l);
    }

    return l;
}

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n, x;
        vector<int> nums;
        cin >> n;
        for (int i = 0; i < n; i++)
        {
            cin >> x;
            nums.push_back(x);
        }
        cout << f(n, nums) << "\n";
    }
}