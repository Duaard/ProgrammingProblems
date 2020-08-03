#include <bits/stdc++.h>

using namespace std;

void solve()
{
    int n, k, l;
    cin >> n >> k >> l;
    vector<int> nums(n + 1);
    vector<int> safe{0};
    for (int i = 1; i <= n; i++)
    {
        cin >> nums[i];

        if (l >= nums[i] + k)
        {
            safe.push_back(i);
        }
    }
    safe.push_back(n + 1);

    bool ok = true;
    for (int s = 1; s < safe.size() && ok; s++)
    {
        // Loop through each pair of safe indices
        // Greedily choose down, no sequence will start with inc order
        // by the definition of our safe space
        int tide = k;
        bool down = true;

        // Get i from prev safe space to current safe space
        for (int i = safe[s - 1] + 1; i < safe[s]; i++)
        {
            // Inc or dec tide according to down
            tide += down ? -1 : 1;

            if (down)
                tide -= max(0, nums[i] + tide - l);
            if (tide < 0 || nums[i] + tide > l)
            {
                ok = false;
                break;
            }

            if (tide == 0)
                down = false;
        }
    }

    if (ok)
    {
        cout << "Yes\n";
    }
    else
    {
        cout << "No\n";
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