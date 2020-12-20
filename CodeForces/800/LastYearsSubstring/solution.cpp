#include <bits/stdc++.h>

using namespace std;

void solve()
{
    int n;
    cin >> n;
    string s;
    cin >> s;

    int left = 0, right = 0;
    string key = "2020";

    int ptr = 0;
    // Check left
    while (ptr < 4 && s[ptr] == key[ptr])
    {
        // cout << s[ptr] << " : " << key[ptr] << "\n";
        left++;
        ptr++;
    }

    ptr = 0;
    // Check right
    while (ptr < 4 && s[n - ptr - 1] == key[4 - ptr - 1])
    {
        // cout << s[n - ptr - 1] << " : " << key[4 - ptr - 1] << "\n";
        right++;
        ptr++;
    }

    if (left + right >= 4)
    {
        cout << "YES\n";
    }
    else
    {
        cout << "NO\n";
    }
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