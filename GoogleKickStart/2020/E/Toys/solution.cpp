#include <bits/stdc++.h>

using namespace std;

void solve()
{
    int n;
    cin >> n;

    vector<long long> r(n), e(n);

    for (int i = 0; i < n; i++)
    {
        cin >> e[i] >> r[i];
    }

    // Round 1 get, cur_time and SUM
    long long sum = 0;
    for (int i = 0; i < n; i++)
    {
        sum += e[i];
    }

    // Round 2
    long long cur_time = sum, max_time = sum;
    int toy_count = 0, best_count = 0;
    priority_queue<pair<long long, int>> pq;

    for (int i = 0; i < n; i++)
    {
        // Add toy's r and e in pq
        pq.push({r[i] + e[i], i});
        // Add toy's e to cur_time
        cur_time += e[i];

        // Check if there's a toy violating rule
        while (!pq.empty() && pq.top().first > sum)
        {
            // Remove toy w/ highest r + e
            int ind = pq.top().second;
            pq.pop();
            cur_time -= 2ll * e[ind];
            sum -= e[ind];
            toy_count++;
        }

        // Update max_time
        if (cur_time > max_time)
        {
            max_time = cur_time;
            best_count = toy_count;
        }
    }
    if (!pq.empty())
    {
        cout << toy_count << " INDEFINITELY\n";
        return;
    }

    cout << best_count << " " << max_time << "\n";
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