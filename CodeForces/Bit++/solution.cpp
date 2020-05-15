#include <bits/stdc++.h>
using namespace std;

int compute(vector<string> operations)
{
    int ans = 0;
    for (string o : operations)
    {
        if (o[1] == '+')
        {
            ans++;
        }
        else
        {
            ans--;
        }
    }
    return ans;
}

int main()
{
    int n;
    cin >> n;
    vector<string> o;
    string input;
    for (int i = 0; i < n; i++)
    {
        cin >> input;
        o.push_back(input);
    }

    cout << compute(o) << "\n";

    return 0;
}