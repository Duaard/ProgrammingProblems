#include <bits/stdc++.h>

using namespace std;

void solve()
{
    int x;
    cin >> x;

    if (x <= 9)
    {
        cout << x << "\n";
        return;
    }
    if (x > 45)
    {
        cout << -1 << "\n";
        return;
    }

    // Build the max sum per digit arr
    vector<int> max_sum;
    int sum = 0;
    for (int i = 9; i > 0; i--)
    {
        sum += i;
        max_sum.push_back(sum);
    }

    // Find the max sum for x
    int ind;
    for (int i = max_sum.size() - 1; i >= 0; i--)
    {
        if (max_sum[i] <= x)
        {
            ind = i;
            break;
        }
    }

    // Find the remaining num
    int rem = 9 - ind;
    for (int i = 0; i < rem; i++)
    {
        if (i + max_sum[ind] == x)
        {
            // Number found
            if (i)
                cout << i;
            for (int j = rem; j <= 9; j++)
            {
                cout << j;
            }
            cout << "\n";

            return;
        }
    }

    cout << -1 << "\n";
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