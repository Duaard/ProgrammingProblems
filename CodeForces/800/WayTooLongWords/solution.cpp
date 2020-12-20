#include <bits/stdc++.h>
using namespace std;

string shorten(string s)
{
    int n = s.size();
    string shortened = s[0] + to_string(n - 2) + s[n - 1];
    return shortened;
}

int main()
{
    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        string s;
        cin >> s;
        if (s.size() > 10)
        {
            cout << shorten(s) << "\n";
        }
        else
        {
            cout << s << "\n";
        }
    }
}