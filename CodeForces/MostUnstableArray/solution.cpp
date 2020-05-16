#include <bits/stdc++.h>
using namespace std;

int unstableArray(int n, int m)
{
    if (n == 1)
    {
        return 0;
    }
    return min(2, n - 1) * m;
}

int main()
{
    int t, n, m;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        cin >> n >> m;
        cout << unstableArray(n, m) << "\n";
    }
    return 0;
}