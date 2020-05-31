#include <bits/stdc++.h>
using namespace std;

int f(int n, int k)
{
    int ans;
    vector<int> factors;

    for (int i = 1; i <= (int)sqrt(n); i++)
    {
        if (n % i == 0)
        {
            factors.push_back(i);
            factors.push_back(n / i);
        }
    }

    sort(factors.rbegin(), factors.rend());
    for (int x : factors)
    {
        if (x <= k)
        {
            return n / x;
        }
    }

    return n;
}

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n, k;
        cin >> n >> k;
        cout << f(n, k) << "\n";
    }
}