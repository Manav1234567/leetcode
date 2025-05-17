# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr and curr.next:
            if curr.val == curr.next.val:
                value = curr.val
                while curr and curr.val == value:
                    curr = curr.next
                if prev:
                    prev.next = curr
                else:
                    head = curr
                continue

            prev = curr
            curr = curr.next

        return head