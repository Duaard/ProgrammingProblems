#include <bits/stdc++.h>

using namespace std;

int n;
long long S;
vector<vector<pair<int, int>>> adj;
vector<int> w, cnt;

long long getDiff(int i)
{
    return w[i] * 1ll * cnt[i] - w[i] / 2 * 1ll * cnt[i];
}

void dfs(int v, int p = -1)
{
    if (adj[v].size() == 1)
        cnt[p] = 1;
    for (auto [to, id] : adj[v])
    {
        if (id == p)
            continue;
        dfs(to, id);
        if (p != -1)
        {
            cnt[p] += cnt[id];
        }
    }
}

void solve()
{
    cin >> n >> S;
    cnt = w = vector<int>(n - 1);
    adj = vector<vector<pair<int, int>>>(n);
    for (int i = 0; i < n - 1; i++)
    {
        int x, y;
        cin >> x >> y >> w[i];
        x--, y--;
        adj[x].push_back({y, i});
        adj[y].push_back({x, i});
    }
    dfs(0);
    // Create a set of pairs to keep track of different weight * leaves
    set<pair<long long, int>> st;
    long long cur = 0;
    for (int i = 0; i < n - 1; i++)
    {
        st.insert({getDiff(i), i});
        cur += w[i] * 1ll * cnt[i];
    }

    int ans = 0;
    while (cur > S)
    {
        // Get the highest diff value
        int id = st.rbegin()->second;
        // Delete the last element
        st.erase(prev(st.end()));
        // Decrease cur by the diff of this id
        cur -= getDiff(id);
        w[id] /= 2;
        // Insert new value for this id
        st.insert({getDiff(id), id});
        // Increment ans
        ans++;
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