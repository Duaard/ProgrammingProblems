#include <bits/stdc++.h>
using namespace std;

int maxSum(vector<int> a, vector<int> b, int n, int k)
{
    sort(begin(a), end(a));
    sort(begin(b), end(b));
    int sum = 0;
    for (int i = 0; i < n; i++)
    {
        int num;
        if (k)
        {
            num = max(b[n - i - 1], a[i]);
            k--;
        }
        else
        {
            num = a[i];
        }
        sum += num;
    }

    return sum;
}

int main()
{
    int t, n, k;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        cin >> n >> k;
        vector<int> a, b;
        int num;
        for (int j = 0; j < n; j++)
        {
            cin >> num;
            a.push_back(num);
        }
        for (int j = 0; j < n; j++)
        {
            cin >> num;
            b.push_back(num);
        }
        cout << maxSum(a, b, n, k) << "\n";
    }
    return 0;
}