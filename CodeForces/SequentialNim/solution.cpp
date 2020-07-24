#include <bits/stdc++.h>

using namespace std;

string FlipWinner(string winner)
{
    if (winner == "First")
    {
        return "Second";
    }
    else
    {
        return "First";
    }
}

void solve()
{
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++)
    {
        cin >> nums[i];
    }

    string winner = "First";
    for (int i = 0; i < n; i++)
    {
        if (nums[i] == 1 && i + 1 != n)
        {
            winner = FlipWinner(winner);
        }
        else
        {
            break;
        }
    }

    cout << winner << "\n";
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