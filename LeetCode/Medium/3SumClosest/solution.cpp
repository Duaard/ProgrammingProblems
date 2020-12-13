class Solution
{
public:
    int threeSumClosest(vector<int> &nums, int target)
    {
        // First sort the array for efficient searching
        sort(nums.begin(), nums.end());

        // Greedily get the best sum
        int diff = INT_MAX;
        int sum;

        // Loop through the array getting left, right
        for (int i = 0; i < nums.size() - 2; i++)
        {
            int left = i + 1;
            int right = nums.size() - 1;

            while (left < right)
            {
                int tmpSum = nums[i] + nums[left] + nums[right];
                if (diff > abs(target - tmpSum))
                {
                    sum = tmpSum;
                    diff = abs(target - tmpSum);
                }
                if (tmpSum > target)
                {
                    // Lessen Sum
                    right--;
                }
                else if (tmpSum < target)
                {
                    // Increase Sum
                    left++;
                }
                else
                {
                    // Found the best sum
                    return tmpSum;
                }
            }
        }

        // Return best sum
        return sum;
    }
};