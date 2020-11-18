#include <bits/stdc++.h>

using namespace std;

long long count_boring(long long n)
{
    long long b = 0;
    int l = to_string(n).size();
    // Add max from other places lower than l
    for (int i = l - 2; i >= 0; i--)
    {
        long long pow5 = pow(5, i);
        b += 5 * pow5;
    }
    // printf("B after default: %i\n", b);

    bool odd = true;
    for (int i = l - 1; i >= 0; i--)
    {
        long long place = pow(10, i);
        long long x = n / place;
        // printf("x: %i\n", x);
        if (i == 0)
        {
            // This the ones place
            long long ones = odd ? (x + 1) / 2 : x / 2 + 1;
            b += ones;
            continue;
        }
        long long p = pow(5, i);
        // printf("b: %i, odd %i x: %i pow: %i\n", b, odd, x, p);
        if (odd)
        {
            b += (x / 2) * p;
            if (x % 2 == 0)
            {
                // Don't add next
                break;
            }
        }
        else
        {
            b += ((x + 1) / 2) * p;
            if (x % 2 != 0)
            {
                // Don't add next
                break;
            }
        }

        odd = !odd;
        n = n % place;
    }

    return b;
}

void solve()
{
    long long l, r;

    cin >> l >> r;

    // Count num of boring from l to r
    // printf("R: %i, L: %i\n", count_boring(r));
    cout << count_boring(r) - count_boring(l - 1) << "\n";
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