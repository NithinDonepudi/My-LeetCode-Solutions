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
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        ListNode* a=head;
        int count=0;
        while(a!=NULL)
        {
            a=a->next;
            count=count+1;
        }
        count=count/2;
        int b=0;
        a=head;
        while(b!=count)
        {
            a=a->next;
            b=b+1;
        }
        return a;
    }
};
