#include <bits/stdc++.h>

using namespace std;

void solve()
{
    int n;
    cin >> n;

    vector<int> h(n);
    for (int i = 0; i < n; i++)
    {
        cin >> h[i];
    }

    int ans = 0;
    for (int i = 1; i < n - 1; i++)
    {
        // printf("i %i i-1 %i i+1 %i\n", i, i - 1, i + 1);
        if (h[i] > h[i - 1] && h[i] > h[i + 1])
        {
            ans++;
        }
    }

    cout << ans << "\n";
}

int main()
{
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++)
    {
        cout << "Case #" << i << ": ";
        solve();
    }
}