#include <bits/stdc++.h>

using namespace std;

void solve()
{
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }

    string word(50, 'a');
    cout << word << "\n";
    for (int i = 0; i < n; i++)
    {
        word[a[i]] = word[a[i]] == 'a' ? 'b' : 'a';
        cout << word << "\n";
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