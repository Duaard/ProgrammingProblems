class Solution
{
public:
    int removeDuplicates(vector<int> &nums)
    {
        if (nums.size() == 0)
        {
            return 0;
        }

        int cur = nums[0];
        int l = 1;

        for (int i = 1; i < nums.size(); i++)
        {
            if (nums[i] != cur)
            {
                nums[l] = nums[i];
                cur = nums[i];
                l++;
            }
        }

        return l;
    }
};