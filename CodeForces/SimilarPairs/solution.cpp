#include <bits/stdc++.h>
using namespace std;

string f(vector<int> &nums)
{
    int odd, even;
    bool extra = false;
    map<int, int> graph;
    for (int x : nums)
    {
        if (x % 2)
        {
            odd++;
        }
        else
        {
            even++;
        }

        if (graph.count(x) == 0)
        {
            graph[x] = 1;
        }

        if (graph.count(x - 1) || graph.count(x + 1))
        {
            extra = true;
        }
    }

    if (odd % 2 == 0 && even % 2 == 0)
    {
        return "YES";
    }
    if (extra)
    {
        return "YES";
    }

    return "NO";
}

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        vector<int> nums(n);
        for (int i = 0; i < n; i++)
        {
            cin >> nums[i];
        }
        cout << f(nums) << "\n";
    }
}