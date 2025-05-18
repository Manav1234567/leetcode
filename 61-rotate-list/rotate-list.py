# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        curr = head
        prev = None
        while curr:
            length += 1
            prev = curr
            curr = curr.next
        
        if (length == 0 or length == 1 or k == 0):
            return head
        k = k % length
        if (k == 0):
            return head
            
        dummy = head
        prev_dummy = None
        for i in range(length - k):
            prev_dummy = dummy
            if dummy:
                dummy = dummy.next

        prev.next = head
        prev_dummy.next = None

        return dummy