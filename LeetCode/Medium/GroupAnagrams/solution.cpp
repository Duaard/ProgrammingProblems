class Solution
{
public:
    vector<vector<string>> groupAnagrams(vector<string> &strs)
    {
        map<string, vector<string>> m;

        for (string str : strs)
        {
            string copy = str;
            sort(str.begin(), str.end());
            m[str] = m.count(str) ? m[str] : vector<string>();
            m[str].push_back(copy);
        }

        vector<vector<string>> ans;
        for (const auto &pair : m)
        {
            ans.push_back(pair.second);
        }
        return ans;
    }
};