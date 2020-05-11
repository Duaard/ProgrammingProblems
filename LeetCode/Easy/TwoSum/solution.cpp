class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        // Hash table approach uses O(n) time but also uses O(n) space

        // Create hash table
        map<int, int> sums;

        // Loop through the numbers populate hash for sum
        for (int i = 0; i < nums.size(); i++)
        {
            if (sums.count(target - nums[i]) > 0)
            {
                return vector<int>{sums[target - nums[i]], i};
            }
            else
            {
                sums[nums[i]] = i;
            }
        }

        // No need for this since we assume that there will always be a solution
        return vector<int>{};
    }
};