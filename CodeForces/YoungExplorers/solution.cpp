#include <bits/stdc++.h>
using namespace std;

int getGroups(vector<int> e)
{
    sort(e.begin(), e.end());
    int c = 0, ans = 0;
    for (int x : e)
    {
        if (++c == x)
        {
            ans++;
            c = 0;
        }
    }

    return ans;
}

int main()
{
    int t;
    cin >> t;
    while (t)
    {
        int n;
        cin >> n;
        vector<int> e(n);
        for (int i = 0; i < n; i++)
        {
            cin >> e[i];
        }

        cout << getGroups(e) << "\n";
        t--;
    }
}