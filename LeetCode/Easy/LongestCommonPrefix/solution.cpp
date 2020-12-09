class Solution
{
public:
    string longestCommonPrefix(vector<string> &strs)
    {
        if (strs.size() == 0)
        {
            return "";
        }

        string common = strs[0];

        for (int i = 1; i < strs.size(); i++)
        {
            common = common.substr(0, min(common.length(), strs[i].length()));
            for (int y = 0; y < common.length(); y++)
            {
                if (common[y] != strs[i][y])
                {
                    common = common.substr(0, y);
                    break;
                }
            }
        }
        return common;
    }
};