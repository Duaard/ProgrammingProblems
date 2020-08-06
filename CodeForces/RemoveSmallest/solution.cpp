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
    bool flag = true;
    sort(nums.begin(), nums.end());

    for (int i = 1; i < n; i++)
    {
        if (nums[i] - nums[i - 1] > 1)
        {
            flag = false;
            break;
        }
    }

    if (flag)
    {
        cout << "YES\n";
    }
    else
    {
        cout << "NO\n";
    }
}

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        solve();
    }
}
