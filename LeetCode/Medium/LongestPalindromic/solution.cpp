class Solution {
public:
    string getPalindrome(string s, int i)
    {
        string ans = "";
        ans += s[i];
        int left = i - 1, right = i + 1;
        // Check for the same char
        while (left >= 0 && s[left] == s[i])
        {
            ans = s[left] + ans;
            left--;
        }
        while (right < s.length() && s[right] == s[i])
        {
            ans += s[right];
            right++;
        }

        // Walk left and right until left != right
        while (left >= 0 && right < s.length() && s[left] == s[right])
        {
            ans = s[left] + ans + s[right];
            left--;
            right++;
        }

        return ans;
    }

    string longestPalindrome(string s)
    {
        string ans = "", pal;
        for (int i = 0; i < s.length(); i++)
        {
            pal = getPalindrome(s, i);
            ans = pal.length() > ans.length() ? pal : ans;
        }
        return ans;
    }
};