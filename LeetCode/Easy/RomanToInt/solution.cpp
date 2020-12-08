class Solution
{
public:
    int romanToInt(string s)
    {
        vector<char> keys = {'I', 'V', 'X', 'L', 'C', 'D', 'M'};
        vector<int> values = {1, 5, 10, 50, 100, 500, 1000};
        unordered_map<char, int> romanNum;

        for (int i = 0; i < keys.size(); i++)
        {
            romanNum[keys[i]] = values[i];
        }

        int ans = 0;
        for (int i = 0; i < s.length(); i++)
        {
            char c = s[i];

            if (i + 1 < s.length() && (c == 'I' || c == 'X' || c == 'C'))
            {
                // Check next
                char next = s[i + 1];
                if (romanNum[c] < romanNum[next])
                {
                    // Subtraction operation
                    ans += romanNum[next] - romanNum[c];
                    i++;
                    continue;
                }
            }
            // Add this num
            ans += romanNum[c];
        }
        return ans;
    }
};