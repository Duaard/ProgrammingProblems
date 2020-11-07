class Solution
{
public:
    vector<vector<int>> merge(vector<vector<int>> &intervals)
    {
        vector<vector<int>> ans;

        sort(intervals.begin(), intervals.end());

        int b, e;

        if (intervals.size() > 0)
        {
            b = intervals[0][0];
            e = intervals[0][1];
        }

        for (vector<int> pair : intervals)
        {
            // Check if this pair is within range
            if (pair[0] <= e)
            {
                e = max(pair[1], e);
            }
            else
            {
                ans.push_back({b, e});
                b = pair[0], e = pair[1];
            }
        }

        if (intervals.size() > 0)
            ans.push_back({b, e});
        return ans;
    }
};