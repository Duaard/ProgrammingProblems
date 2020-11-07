class Solution
{
public:
    void sortColors(vector<int> &nums)
    {
        map<int, int> m;

        for (int x : nums)
        {
            m[x]++;
        }

        int count = 0;
        for (const auto [key, value] : m)
        {
            for (int i = 0; i < value; i++)
            {
                nums[i + count] = key;
            }
            count += value;
        }
    }
};