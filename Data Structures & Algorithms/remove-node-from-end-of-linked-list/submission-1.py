# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head

        len = 0
        while node:
            node = node.next
            len += 1
        if len-n == 0:
            return head.next

        len = len - n

        node = head
        while node:
            if len == 1:
                node.next = node.next.next
            len -= 1
            node = node.next
        return head