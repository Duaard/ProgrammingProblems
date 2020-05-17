#include <bits/stdc++.h>
using namespace std;

long long getAdd(long long x)
{
    long long h = 0, l = 10;

    while (x)
    {
        long long d = x % 10;
        x /= 10;
        h = max(h, d);
        l = min(l, d);
    }
    return h * l;
}

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        long long a, k;
        cin >> a >> k;

        while (--k)
        {
            long long x = getAdd(a);
            if (x == 0)
            {
                break;
            }
            a += x;
        }

        cout << a << "\n";
    }
}