class Solution
{
public:
    void moveZeroes(vector<int> &nums)
    {
        // Points to the last non zero index
        int pointer = 0;
        int n = nums.size();
        a for (int x : nums)
        {
            if (x != 0)
            {
                // Move this num to the last index pos for non-zero
                nums[pointer] = x;
                pointer++;
            }
        }

        for (int i = pointer; i < n; i++)
        {
            // Fill in 0 values
            nums[i] = 0;
        }
    }
};