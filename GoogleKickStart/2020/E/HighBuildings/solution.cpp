#include <bits/stdc++.h>

using namespace std;

void solve()
{
    int N, A, B, C;
    cin >> N >> A >> B >> C;

    vector<int> buildings(N, 0);

    int left = (A - C) + (B - C) + C;
    if ((left == 1 && N != 1) || left > N)
    {
        cout << "IMPOSSIBLE\n";
        return;
    }

    for (int i = 0; i < A - C; i++)
    {
        buildings[i]++;
    }
    for (int i = 0; i < B - C; i++)
    {
        buildings[N - 1 - i]++;
    }

    int c = C;

    if (B - C == 0)
    {
        buildings[N - 1] = N;
        c--;
    }

    for (int i = A - C; c > 0; i++)
    {
        buildings[i] = N;
        c--;
    }

    for (int x : buildings)
    {
        int ans = x;
        if (N != 2)
        {
            ans = x == N ? x : x + 1;
        }
        cout << ans << " ";
    }
    cout << "\n";
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