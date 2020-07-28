class Solution
{
public:
    int maxProfit(vector<int> &prices)
    {
        int stock = 0, cash = INT_MIN;
        for (int x : prices)
        {
            cash = max(cash, stock - x);
            stock = max(stock, cash + x);
        }

        return stock;
    }
};