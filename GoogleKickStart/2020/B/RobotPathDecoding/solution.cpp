#include <bits/stdc++.h>

using namespace std;

pair<int, int> handle_movement(char x)
{
    switch (x)
    {
    case 'N':
        return {0, -1};
    case 'S':
        return {0, 1};
    case 'E':
        return {1, 0};
    case 'W':
        return {-1, 0};
    default:
        return {0, 0};
    }
}

pair<long long, long long> get_value(int &i, string s)
{
    bool movement = true;
    long long w = 0, h = 0;
    while (movement && i < s.length())
    {
        pair<int, int> m = handle_movement(s[i]);
        if (m.first == 0 && m.second == 0)
        {
            // Special instruction
            if (s[i] == ')')
            {
                // End of instruction return val
                //cout << "RETURN AT " << i << "\n";
                return {w, h};
            }

            string multi_str = "";
            while (s[i] != '(')
            {
                multi_str += s[i];
                i++;
            }
            i++;
            //cout << "MULTI STR: " << multi_str << "\n";
            long long multi = stoll(multi_str);
            pair<long long, long long> special = get_value(i, s);

            m.first = multi * special.first % (long long)1e9;
            m.first = m.first < 0 ? m.first += (long long)1e9 : m.first;

            m.second = multi * special.second % (long long)1e9;
            m.second = m.second < 0 ? m.second += (long long)1e9 : m.second;
        }

        w += m.first;
        h += m.second;
        i++;
    }
    return {w, h};
}

void solve()
{
    string s;
    cin >> s;

    long long w = 0, h = 0;
    int i = 0;
    pair<long long, long long> ans;
    ans = get_value(i, s);

    w = ans.first % (long long)1e9;
    w = w < 0 ? w += (long long)1e9 : w;

    h = ans.second % (long long)1e9;
    h = h < 0 ? h += (long long)1e9 : h;

    cout << w + 1ll << " " << h + 1ll << "\n";

    // w = w >= 0 ? 1 + ans.first : (long long)1e9 + 1ll + w;
    // h = h >= 0 ? 1 + ans.second : (long long)1e9 + 1ll + h;
    // cout << w << " " << h << "\n";
}

int main()
{
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++)
    {
        cout << "Case #" << i << ": ";
        solve();
    }
}