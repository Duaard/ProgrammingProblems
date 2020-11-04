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
private:
    // Merges two sorted lists
    ListNode *merge(ListNode *l1, ListNode *l2)
    {
        ListNode dummy = ListNode();
        ListNode *temp = &dummy;

        while (l1 && l2)
        {
            if (l1->val < l2->val)
            {
                temp->next = l1;
                l1 = l1->next;
            }
            else
            {
                temp->next = l2;
                l2 = l2->next;
            }
            temp = temp->next;
        }

        if (l1)
        {
            temp->next = l1;
        }
        else
        {
            temp->next = l2;
        }

        return dummy.next;
    }

    ListNode *mergeSort(ListNode *h)
    {
        if (!h || !h->next)
            return h;
        // Find mid
        ListNode *m = mid(h);

        // Sort Left
        ListNode *left = mergeSort(h);
        // Sort Right
        ListNode *right = mergeSort(m);

        // Merge Left and Right
        return merge(left, right);
    }

    ListNode *mid(ListNode *h)
    {
        ListNode *m = nullptr;

        while (h && h->next)
        {
            m = (m == nullptr) ? h : m->next;
            h = h->next->next;
        }
        ListNode *mid = m->next;
        m->next = nullptr;

        return mid;
    }

public:
    ListNode *sortList(ListNode *head)
    {
        return mergeSort(head);
    }
}