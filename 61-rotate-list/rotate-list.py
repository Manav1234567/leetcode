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
        
        if (length <= 1):
            return head
        k = k % length
        if (k == 0):
            return head

        prev.next = head
        prev = None
        curr = head
        for _ in range(length - k):
            prev = curr
            curr = curr.next

        prev.next = None

        return curr