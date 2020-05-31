#include <bits/stdc++.h>
using namespace std;

string f(vector<string> &m)
{
    int n = m.size();
    // Loop each row
    for (int row = 0; row < n; row++)
    {
        // Loop each col
        for (int col = 0; col < n; col++)
        {
            if (m[row][col] == '1')
            {
                // Check if bottom or right is 1 or is boundary
                if ((row != n - 1 && col != n - 1) && (m[row + 1][col] != '1' && m[row][col + 1] != '1'))
                {
                    return "NO";
                }
            }
        }
    }
    return "YES";
}

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        vector<string> m(n);
        for (int i = 0; i < n; i++)
        {
            cin >> m[i];
        }
        cout << f(m) << "\n";
    }
}