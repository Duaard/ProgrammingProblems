#include <bits/stdc++.h>

using namespace std;

void solve()
{
    int n, x, y;
    cin >> n >> x >> y;

    vector<int> nums(n);
    vector<int> a(n);

    // List of colors with frequency n
    vector<vector<int>> freq(n + 1);
    // List of index color n is at
    vector<vector<int>> ind(n + 1 + 1);
    // Check if index already at mismatch
    vector<bool> mis(n);

    for (int i = 0; i < n; i++)
    {
        cin >> nums[i];
        mis[i] = false;
        // Record index i at color nums[i]
        ind[nums[i]].push_back(i);
    }

    // Loop through all color and record its frequency
    for (int i = 1; i <= n + 1; i++)
    {
        freq[ind[i].size()].push_back(i);
    }

    // Start from most freq and find best possible x pos
    int f = n;
    for (int k = 0; k < x; k++)
    {
        while (freq[f].empty())
        {
            f--;
        }

        // Get the color with most freq
        int col = freq[f].back();
        int idx = ind[col].back();

        // Record the answer
        a[idx] = col;
        // Update freq and ind values
        ind[col].pop_back();
        freq[f].pop_back();
        freq[f - 1].push_back(col);
    }

    // Get the next highest frequency
    while (f > 0 && freq[f].empty())
        f--;

    // 2n - x - y == (n - x) + (n - y)
    if (2 * f > 2 * n - x - y)
    {
        cout << "NO\n";
        return;
    }

    // Get all remaining indices and put it in a vector
    vector<int> ve;
    for (int i = 1; i <= f; i++)
    {
        for (int color : freq[i])
        {
            ve.insert(ve.end(), ind[color].begin(), ind[color].end());
        }
    }

    int mismatch = n - y;
    auto makemismatch = [&](int i) {
        a[i] = freq[0][0];
        mismatch--;
        mis[i] = true;
    };

    for (int i = 0; i < n - x; i++)
    {
        a[ve[i]] = nums[ve[(i + (n - x) / 2) % (n - x)]];
        if (a[ve[i]] == nums[ve[i]])
        {
            makemismatch(ve[i]);
        }
    }

    for (int i = 0; mismatch > 0; i++)
    {
        if (!mis[ve[i]])
            makemismatch(ve[i]);
    }

    cout << "YES\n";
    for (int i = 0; i < n; i++)
    {
        cout << a[i] << ' ';
    }
    cout << '\n';
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
