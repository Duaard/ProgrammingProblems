class Solution
{
public:
    int lastStoneWeight(vector<int> &stones)
    {
        sort(stones.begin(), stones.end());

        while (stones.size() > 1)
        {
            int s1 = stones.back();
            stones.pop_back();
            int s2 = stones.back();
            stones.pop_back();

            int ans = s1 - s2;

            if (ans)
            {
                stones.push_back(ans);
            }
            sort(stones.begin(), stones.end());
        }

        if (stones.size())
        {
            return stones.back();
        }

        return 0;
    }
};