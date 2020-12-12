class Solution
{
public:
    vector<vector<int>> threeSum(vector<int> &nums)
    {
        if (nums.size() < 3)
        {
            vector<vector<int>> tmp;
            return tmp;
        }
        // Sort the array
        sort(nums.begin(), nums.end());
        set<vector<int>> ans;

        // Loop through each number
        for (int i = 0; i < nums.size() - 2; i++)
        {
            int left = i + 1;
            int right = nums.size() - 1;

            while (left < right)
            {
                int sum = nums[left] + nums[i] + nums[right];
                if (sum == 0)
                {
                    // Add this to possible answers
                    vector<int> tmp = {nums[i], nums[left], nums[right]};
                    ans.insert(tmp);
                    right--;
                    left++;
                }
                else if (sum > 0)
                {
                    // Lessen the sum
                    right--;
                }
                else
                {
                    // Increase the sum
                    left++;
                }
            }
        }

        vector<vector<int>> toVector;
        copy(ans.begin(), ans.end(), back_inserter(toVector));
        return toVector;
    }
};