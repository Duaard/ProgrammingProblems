class Solution
{
public:
    vector<vector<int>> ans;

    void dfsRecursive(vector<vector<int>> &graph, int index, vector<int> &path, int end)
    {
        // Add this to the current path
        path.push_back(index);
        if (index == end)
        {
            ans.push_back(path);
        }

        for (auto c : graph[index])
        {
            dfsRecursive(graph, c, path, end);
        }
        path.pop_back();
    }
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>> &graph)
    {
        int end = graph.size() - 1;

        for (auto c : graph[0])
        {
            // Create a new path
            vector<int> path(0);
            path.push_back(0);
            dfsRecursive(graph, c, path, end);
        }
        return ans;
    }
};