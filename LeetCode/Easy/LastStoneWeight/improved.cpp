class Solution
{
public:
    int lastStoneWeight(vector<int> &stones)
    {
        priority_queue<int> pq;

        for (int s : stones)
        {
            pq.push(s);
        }

        while (pq.size() > 1)
        {
            int s1 = pq.top();
            pq.pop();
            int s2 = pq.top();
            pq.pop();

            int ans = s1 - s2;
            if (ans)
            {
                pq.push(ans);
            }
        }

        if (pq.size())
        {
            return pq.top();
        }

        return 0;
    }
};