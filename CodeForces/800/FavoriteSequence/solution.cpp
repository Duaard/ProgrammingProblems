#include <bits/stdc++.h>

using namespace std;

void solve()
{
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++)
    {
        cin >> nums[i];
    }

    int left = 0, right = n - 1;

    while (left <= right)
    {
        cout << nums[left] << " ";

        if (left != right)
        {
            cout << nums[right] << " ";
        }

        left++;
        right--;
    }
    cout << "\n";
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