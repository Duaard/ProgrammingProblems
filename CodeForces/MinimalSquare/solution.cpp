#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int a, b;
        cin >> a >> b;
        int h = max(a, b);
        int l = min(a, b);
        int ans = max(h, 2 * l);
        cout << ans * ans << "\n";
    }
}