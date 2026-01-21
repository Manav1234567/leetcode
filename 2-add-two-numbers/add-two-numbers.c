/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* helper(struct ListNode* l1, struct ListNode* l2, int carry);
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    return helper(l1, l2, 0);
}

struct ListNode* helper(struct ListNode* l1, struct ListNode* l2, int carry) {
    printf("%d\n", carry);

    if (l1 == NULL && l2 == NULL) {
        if (carry != 0) {
            struct ListNode *ans = malloc(sizeof(struct ListNode));
            ans->val = carry;
            ans->next = NULL;
            return ans;
        }
        return NULL;
    } 

    int next_carry = 0;
    
    struct ListNode *ans = malloc(sizeof(struct ListNode));
    if (l1 == NULL && l2 != NULL) {
        ans->val = l2->val + carry;
        next_carry = ans->val / 10;
        ans->val %= 10;
        ans->next = helper(l1, l2->next, next_carry);
    } else if (l1 != NULL && l2 == NULL) {
        ans->val = l1->val + carry;
        next_carry = ans->val / 10;
        ans->val %= 10;
        ans->next = helper(l1->next, l2, next_carry);
    } else {
        ans->val = l1->val + l2->val + carry;
        next_carry = ans->val / 10;
        ans->val %= 10;
        ans->next = helper(l1->next, l2->next, next_carry);
    }

    return ans;
}