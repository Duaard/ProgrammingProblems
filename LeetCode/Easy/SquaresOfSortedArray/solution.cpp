class Solution
{
public:
    vector<int> sortedSquares(vector<int> &nums)
    {
        // O(log N) Priority Queue
        priority_queue<int, vector<int>, greater<int>> pq;
        for (auto n : nums)
        {
            pq.push(n * n);
        }
        vector<int> ans;
        while (!pq.empty())
        {
            ans.push_back(pq.top());
            pq.pop();
        }
        return ans;
    }
};