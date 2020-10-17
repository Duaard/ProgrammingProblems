#include <bits/stdc++.h>

using namespace std;

void solve()
{
    int n, b;

    cin >> n >> b;

    vector<int> houses(n);
    priority_queue<int, vector<int>, greater<int>> pq;

    for (int i = 0; i < n; i++)
    {
        cin >> houses[i];
        pq.push(houses[i]);
    }

    int sum = 0;
    int ans = 0;
    while (sum + pq.top() <= b && !pq.empty())
    {
        sum += pq.top();
        pq.pop();
        ans++;
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