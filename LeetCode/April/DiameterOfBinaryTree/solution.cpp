/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution
{
public:
    pair<int, int> dfs(TreeNode *node)
    {
        // <diameter, depth>
        if (node == NULL)
        {
            return {0, 0};
        }
        pair<int, int> l = dfs(node->left);
        pair<int, int> r = dfs(node->right);

        int d = max({l.first, r.first, l.second + r.second});
        return {d, max(l.second, r.second) + 1};
    }

    int diameterOfBinaryTree(TreeNode *root)
    {
        return dfs(root).first;
    }
};