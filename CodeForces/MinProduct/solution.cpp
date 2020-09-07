#include <bits/stdc++.h>

using namespace std;

void solve()
{
    int a, b, x, y, n;

    cin >> a >> b >> x >> y >> n;

    int dist_a, dist_b, extra_a, extra_b;
    long long prod_a, prod_b;
    dist_a = a - x;
    dist_b = b - y;
    extra_a = n > dist_a ? n - dist_a : 0;
    extra_b = n > dist_b ? n - dist_b : 0;
    dist_a = max(0, dist_a - n);
    dist_b = max(0, dist_b - n);
    //cout << a << " " << b << " " << x << " " << y << " " << n << "\n";
    //cout << "Distance: " << dist_a << " " << dist_b << "\n";
    //cout << "Extra: " << extra_a << " " << extra_b << "\n";

    prod_a = (x + dist_a * 1ll) * (y * 1ll + max(0, (b - y - extra_a)));
    prod_b = (y + dist_b * 1ll) * (x * 1ll + max(0, (a - x - extra_b)));
    cout << min(prod_a, prod_b) << "\n";
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