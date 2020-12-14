/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution
{
public:
    ListNode *mergeKLists(vector<ListNode *> &lists)
    {
        // O(N K)

        ListNode *beg = nullptr;
        ListNode *tmp = new ListNode;
        // Look for the min node
        while (true)
        {
            int min = INT_MAX;
            int minNode = -1;
            for (int i = 0; i < lists.size(); i++)
            {
                if (lists[i] && lists[i]->val < min)
                {
                    min = lists[i]->val;
                    minNode = i;
                }
            }
            if (minNode == -1)
            {
                break;
            }
            if (beg == nullptr)
            {
                beg = lists[minNode];
            }
            tmp->next = lists[minNode];
            tmp = lists[minNode];

            // Increment this node
            lists[minNode] = lists[minNode]->next;
        }
        return beg;
    }
};