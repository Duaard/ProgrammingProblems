class Solution
{
public:
    int myAtoi(string s)
    {
        int num = 0;
        bool intFound = false;
        int sign = 1;
        for (char c : s)
        {
            if (!intFound)
            {
                // Disregard white space
                if (c == ' ')
                    continue;
                // Sign
                else if (c == '+' || c == '-')
                {
                    sign = c == '-' ? -1 : 1;
                    intFound = true;
                }
                // Valid int char
                else if (isdigit(c))
                {
                    intFound = true;
                    num += (c - '0') * sign;
                }
                // Not valid num
                else
                    break;
            }
            else
            {
                // Not valid num, break the sequence
                if (!isdigit(c))
                {
                    break;
                }
                else
                {
                    // Add this char to ans;
                    // Check if this would cause overflow
                    int n = (c - '0') * sign;
                    if (num > INT_MAX / 10 || (num == INT_MAX / 10 && n > 7))
                    {
                        return INT_MAX;
                    }
                    if (num < INT_MIN / 10 || (num == INT_MIN / 10 && n < -8))
                    {
                        return INT_MIN;
                    }
                    num *= 10;
                    num += n;
                }
            }
        }

        return num;
    }
};