# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        prev = None
        temp = None
        tempn = None

        while head and head.next:
            temp = head
            tempn = head.next
            head.next = prev
            prev = temp
            head = tempn
        head.next = prev
        return head