# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head: return None

        def reverse(head, k):
            if k == 0: return head, head.next if head else None
            if not head or not head.next: return head, None

            curr, tail = reverse(head.next, k-1)
            head.next.next = head
            head.next = tail
            return curr, tail

        gap = right - left
        if gap == 0: return head

        if left == 1: return reverse(head, gap)[0]
        
        curr = head
        while curr and left - 2 > 0:
            curr = curr.next
            left -= 1
        curr.next, _ = reverse(curr.next, gap)
        return head