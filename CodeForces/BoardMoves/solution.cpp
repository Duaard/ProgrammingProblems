#include <bits/stdc++.h>
using namespace std;

long long minMoves(long long n)
{
    if (n == 1)
    {
        return 0;
    }
    n /= 2;
    long long ans = 8 * ((n * (n + 1) * (2 * n + 1)) / 6);
    return ans;
}

int main()
{
    int t;
    cin >> t;
    while (t)
    {
        long long n;
        cin >> n;
        cout << minMoves(n) << "\n";
        t--;
    }
}