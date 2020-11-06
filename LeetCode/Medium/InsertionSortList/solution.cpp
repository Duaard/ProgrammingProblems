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
    ListNode *insertionSortList(ListNode *head)
    {
        ListNode *curr = head ? head->next : nullptr;
        ListNode *last = head;

        // Loop through each node
        while (curr)
        {
            ListNode *next = curr->next;
            ListNode *n = head;
            ListNode *prev = nullptr;

            // Point last to curr's next
            last->next = next;

            // Check if curr is greater than last
            if (curr->val > last->val)
            {
                // Point last to this val and continue
                curr->next = last->next;
                last->next = curr;
                last = curr;
            }
            else
            {
                // Look for currs position
                while (curr->val > n->val)
                {
                    prev = n;
                    n = n->next;
                }

                if (!prev)
                {
                    // Curr is the new head
                    head = curr;
                }
                else
                {
                    // Point prev to curr
                    prev->next = curr;
                }
                curr->next = n;
            }

            curr = next;
        }

        return head;
    }
};