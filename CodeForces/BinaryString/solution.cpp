#include <bits/stdc++.h>

using namespace std;

void solve()
{
    int n;
    cin >> n;
    string s;
    cin >> s;
    vector<int> place(n);

    int z = 0, o = 0, k = 0, i = 0;
    vector<int> p_z, p_o;
    for (char c : s)
    {
        int p = 0;
        if (c == '0')
        {
            if (z)
            {
                p = p_z.back();
                p_o.push_back(p);
                p_z.pop_back();
                z--;
            }
            else
            {
                k++;
                p = k;
                p_o.push_back(p);
            }
            o++;
        }
        else
        {
            if (o)
            {
                p = p_o.back();
                p_z.push_back(p);
                p_o.pop_back();
                o--;
            }
            else
            {
                k++;
                p = k;
                p_z.push_back(p);
            }
            z++;
        }
        place[i] = p;
        i++;
    }
    cout << k << "\n";
    for (int x : place)
    {
        cout << x << " ";
    }
    cout << "\n";
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
