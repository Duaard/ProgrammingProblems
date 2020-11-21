class Solution
{
public:
    int lengthOfLongestSubstring(string s)
    {
        // Greedily get longest substring
        int max_len = 0;
        // Create a map to keep track of current letters encountered and it's index
        unordered_map<char, int> m;
        int curr = 0;
        int left = 0;
        // Loop through every char and keep track of longest substring
        for (int i = 0; i < s.size(); i++)
        {
            // Check if this char has been encountered
            if (m.count(s[i]) > 0)
            {
                left = max(m[s[i]], left);
            }

            curr = i - left;
            max_len = max(max_len, curr + 1);
            // Save the index of this char
            m[s[i]] = i + 1;
        }

        return max_len;
    }
};