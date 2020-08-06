#include <bits/stdc++.h>

using namespace std;

void solve()
{
    int n;
    cin >> n;
    vector<int> nums(n);

    unordered_map<int, int> m;
    set<int> nu;
    for (int i = 0; i < n; i++)
    {
        cin >> nums[i];
        m[nums[i]]++;
        nu.insert(nums[i]);
    }
    set<int> s;
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            s.insert(nums[i] + nums[j]);
        }
    }

    int ans = 0;
    for (int sum : s)
    {
        int tmp_ans = 0;
        for (int x : nu)
        {
            int tmp = sum - x;
            tmp_ans += min(m[tmp], m[x]);
        }
        ans = max(ans, tmp_ans / 2);
    }

    cout << ans << "\n";
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