class Solution
{
public:
    string convert(string s, int numRows)
    {
        string zigzag = "";
        if (numRows == 1)
            return s;
        // For n rows
        for (int i = 0; i < numRows; i++)
        {
            // Get all letters for this row
            int j = i;
            int mul_next = 0, mul_inv = 0;
            int next = numRows - 1 - i;
            int next_inv = numRows - 1 - next;
            bool inv = false;
            while (j < s.length())
            {
                // Add next
                j = i + mul_next * (2 * next);
                // Add next_inv
                j += mul_inv * (2 * next_inv);
                if (j >= s.length())
                {
                    break;
                }
                zigzag += s[j];

                if (!inv)
                {
                    mul_next++;
                }
                else
                {
                    mul_inv++;
                }

                if (next == 0 || next_inv == 0)
                {
                    mul_next = max(mul_next, mul_inv);
                    mul_inv = max(mul_inv, mul_next);
                }
                inv = !inv;
            }
        }
        return zigzag;
    }
};