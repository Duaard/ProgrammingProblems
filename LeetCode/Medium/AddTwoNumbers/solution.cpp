#include "../../../stdc++.h">
using namespace std;

struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

ListNode *addTwoNumbers(ListNode *l1, ListNode *l2)
{
    ListNode *sum = new ListNode();
    ListNode *start = sum;
    int val;
    int carry = 0;

    while (l1 || l2)
    {
        val = carry + l1->val + l2->val;
        if (val >= 10)
        {
            val %= 10;
            carry = 1;
        }
        else
        {
            carry = 0;
        }
        sum->val = val;

        l1 = l1->next;
        l2 = l2->next;

        if (l1 || l2 || carry)
        {
            sum->next = new ListNode();
            sum = sum->next;
        }
    }

    return start;
}

ListNode *vectorToList(vector<int> nums)
{
    ListNode *node;
    ListNode *start;

    for (int num : nums)
    {
        node->next = new ListNode(num);
        node = node->next;
        if (start == NULL)
        {
            start = node;
        }
    }

    return start;
}

vector<int> listToVector(ListNode *l)
{
    vector<int> n;
    while (l->next)
    {
        n.push_back(l->val);
    }
    return n;
}

int main()
{
    int m, n;
    vector<int> mm, nn;
    int inp;

    cin >> m >> n;
    for (int i = 0; i < m; i++)
    {
        cin >> inp;
        mm.push_back(inp);
    }
    for (int i = 0; i < n; i++)
    {
        cin >> inp;
        nn.push_back(inp);
    }
    ListNode *l1 = vectorToList(mm);
    ListNode *l2 = vectorToList(nn);

    vector<int> ans = listToVector(addTwoNumbers(l1, l2));
    for (int i = 0; ans.size(); i++)
    {
        cout << ans[i] << " ";
    }

    return 0;
}