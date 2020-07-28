#include "../../stdc++.h"
using namespace std;

void f()
{
    int n, m, a, b;
    cin >> n >> m >> a >> b;

    if (n * a != m * b)
    {
        cout << "NO\n";
        return;
    }

    vector<string> ans(n);
    vector<int> c_count(m);
    int r_count = 0;
    int shift = 0;

    // 3 6 2 1
    // 1 1 0 0 0 0
    // 0 0 1 1 0 0
    // 0 0 0 0 1 1

    // 5 5 3 3

    // 7 14 10 5

    // 1 1 1 0 0
    // 1 1 1 0 0
    // 1 1 1 0 0
    // 0 0 0 1 1
    // 0 0 0 1 1

    // 1 1 1 0 0
    // 0 1 1 1 0
    // 0 0 1 1 1
    // 1 0 0 1 1
    // 1 1 0 0 1

    for (int row = 0; row < n; row++)
    {
        r_count = 0;
        ans[row] = string(m, ' ');
        shift = row;
        for (int col = 0; col < m; col++)
        {
            if (r_count < a)
            {
                ans[row][shift % m] = '1';
                c_count[col]++;
                r_count++;
            }
            else
            {
                ans[row][shift % m] = '0';
            }
            shift++;
        }
    }

    // Print Answer
    cout << "YES\n";
    for (string w : ans)
    {
        cout << w << "\n";
    }
}

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        f();
    }
}