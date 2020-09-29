#include <bits/stdc++.h>

using namespace std;

void solve()
{
    int n, k;
    cin >> n >> k;

    vector<int> s(n), e(n);
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> p_q;

    for (int i = 0; i < n; i++)
    {
        cin >> s[i] >> e[i];
        p_q.push({s[i], i});
    }

    long long next = 0, ans = 0;

    while (!p_q.empty())
    {
        int ind = p_q.top().second;
        if (next >= e[ind])
        {
            // Proceed
        }
        else
        {
            // Increase answer and add k to next
            int mul = 1;
            if (next > s[ind])
            {
                mul = (e[ind] - next - 1) / k;
                mul++;
                next += k * mul;
            }
            else
            {
                mul = (e[ind] - s[ind] - 1) / k;
                mul++;
                next = s[ind] + (k * mul);
            }

            ans += mul;
        }

        p_q.pop();
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