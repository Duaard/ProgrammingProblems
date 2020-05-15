class Solution
{
public:
    int maxProfit(vector<int> &prices)
    {
        int min = INT_MAX, max = INT_MIN;
        int profit = 0;
        for (int p : prices)
        {
            // If p became lower than max sell at max and set new min
            if (p < max)
            {
                profit += max - min;
                max = INT_MIN;
                min = p;
            }

            min = p < min ? p : min;
            max = p > max ? p : max;
        }

        if (min != max)
        {
            profit += max - min;
        }

        return profit;
    }
};