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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int pos = 0;
        ListNode *curr = head;
        while (curr != nullptr) {
            pos += 1;
            curr = curr->next;
        }
        if (pos == 0 || n > pos) {
            return NULL;
        }
        pos -= n;
        curr = head;
        
        if (pos == 0) {
            head = head->next;
            delete(curr);
            return head;
        }
        for (; pos > 1 && curr->next != NULL; pos--) {
            curr = curr->next;
        }
        ListNode *temp = curr->next;
        if (curr->next != NULL) {
        curr->next = curr->next->next;
        } else {
            curr->next = NULL;
        }
        delete(temp);
        return head;
    }
};