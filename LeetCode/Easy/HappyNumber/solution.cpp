class Solution
{
public:
    bool isHappy(int n)
    {
        int sum, d;
        for (int i = 0; i < 100000; i++)
        {
            sum = 0;
            while (n)
            {
                d = n % 10;
                n /= 10;
                sum += d * d;
            }
            if (sum == 1)
            {
                return true;
            }
            else
            {
                n = sum;
            }
        }
        return false;
    }
};