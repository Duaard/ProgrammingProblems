#include <bits/stdc++.h>

using namespace std;

vector<vector<pair<int, int>>> adj;
vector<int> cnt, w, cost;

long long diff(int i)
{
    return w[i] * 1ll * cnt[i] - w[i] / 2 * 1ll * cnt[i];
}

void dfs(int v, int p = -1)
{
    if (adj[v].size() == 1)
    {
        cnt[p] = 1;
    }
    for (auto [to, ind] : adj[v])
    {
        if (p == ind)
            continue;
        dfs(to, ind);
        if (p != -1)
            // Add the leaves of child to parent
            cnt[p] += cnt[ind];
    }
}

void solve()
{
    int n;
    long long S;
    cin >> n >> S;

    cnt = w = cost = vector<int>(n - 1);
    adj = vector<vector<pair<int, int>>>(n);
    for (int i = 0; i < n - 1; i++)
    {
        int x, y;
        cin >> x >> y >> w[i] >> cost[i];
        --x;
        --y;
        adj[x].push_back({y, i});
        adj[y].push_back({x, i});
    }
    dfs(0);

    // Get st1 cur1 and st2 cur2
    set<pair<long long, int>> st1, st2;
    long long cur1 = 0, cur2 = 0;
    for (int i = 0; i < n - 1; i++)
    {
        if (cost[i] == 1)
        {
            st1.insert({diff(i), i});
            cur1 += w[i] * 1ll * cnt[i];
        }
        else
        {
            st2.insert({diff(i), i});
            cur2 += w[i] * 1ll * cnt[i];
        }
    }

    // Get Vector 1
    vector<long long> v1;
    v1.push_back(cur1);
    while (cur1 > 0)
    {
        int id = st1.rbegin()->second;
        cur1 -= diff(id);
        v1.push_back(cur1);
        w[id] /= 2;
        st1.erase(prev(st1.end()));
        st1.insert({diff(id), id});
    }
    // Get Vector 2
    vector<long long> v2;
    v2.push_back(cur2);
    while (cur2 > 0)
    {
        int id = st2.rbegin()->second;
        st2.erase(prev(st2.end()));
        cur2 -= diff(id);
        v2.push_back(cur2);
        w[id] /= 2;
        st2.insert({diff(id), id});
    }
    // Perform 2 pointers, first is i moving to left of v1
    // second dis p moving to right of v2, get greedy answer
    int p = v2.size() - 1;
    int ans = INT_MAX;
    for (int i = 0; i < v1.size(); i++)
    {
        while (p > 0 && v1[i] + v2[p - 1] <= S)
        {
            // Move p to the left
            p--;
        }
        if (v1[i] + v2[p] <= S)
        {

            ans = min(ans, i + (2 * p));
        }
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