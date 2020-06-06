#include <bits/stdc++.h>
using namespace std;

bool check(string w, string ans)
{
    // Check if the two given strings only differ in 1 char
    int n = w.size();
    int counter = 0;
    for (int i = 0; i < n; i++)
    {
        counter = w[i] != ans[i] ? counter + 1 : counter;

        if (counter >= 2)
        {
            return false;
        }
    }

    return true;
}

string f(vector<string> &w)
{
    int n = w[0].size();
    // Loop through each char pos
    for (int i = 0; i < n; i++)
    {
        // Make a copy of the first string as possible answer
        string ans = w[0];
        // Loop through each possible answer
        for (char a = 'a'; a <= 'z'; a++)
        {
            // Set ith char to a as possible answer
            ans[i] = a;

            bool flag = true;
            // Check all strings if this ans can be the answer
            for (string word : w)
            {
                flag = check(word, ans);
                if (!flag)
                    break;
            }
            if (flag)
                return ans;
        }
    }

    return "-1";
}

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n, m;
        cin >> n >> m;
        vector<string> w(n);
        for (int i = 0; i < n; i++)
        {
            cin >> w[i];
        }

        cout << f(w) << "\n";
    }
}