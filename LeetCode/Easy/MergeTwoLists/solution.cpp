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
    ListNode *mergeTwoLists(ListNode *l1, ListNode *l2)
    {
        ListNode *beg = nullptr;
        ListNode *curr = new ListNode;
        while (l1 || l2)
        {
            ListNode *tmp;
            if (!l1)
            {
                tmp = l2;
                l2 = l2->next;
            }
            else if (!l2)
            {
                tmp = l1;
                l1 = l1->next;
            }
            else if (l1->val < l2->val)
            {
                // Get l1
                tmp = l1;
                l1 = l1->next;
            }
            else
            {
                // Get l2
                tmp = l2;
                l2 = l2->next;
            }

            curr->next = tmp;
            curr = tmp;

            if (beg == nullptr)
            {
                beg = tmp;
            }
        }
        return beg;
    }
};