class Solution
{
public:
    string f(string s)
    {
        string t;
        for (char c : s)
        {
            if (c == '#')
            {
                if (t.size() > 0)
                {
                    t.pop_back();
                }
            }
            else
            {
                t += c;
            }
        }
        return t;
    }
    bool backspaceCompare(string S, string T)
    {
        return f(S) == f(T);
    }
};