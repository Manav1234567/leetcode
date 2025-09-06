# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head, k):
            if k == 1: return head, head.next if head else None
            if not head or not head.next: return head, None

            curr, tail = reverse(head.next, k-1)
            head.next.next = head
            head.next = tail
            return curr, tail

        if not head or k == 1: return head

        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1

        if length >= k:
            head, _ = reverse(head, k)
            length -= k

        curr = head
        while curr and length >= k:
            for _ in range(k - 1):
                curr = curr.next
            curr.next, _ = reverse(curr.next, k)
            length -= k
            curr = curr.next
        return head