# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        all_empty = True

        for node in lists:
            if node != None:
                all_empty = False

        if all_empty:
            return None

        arr = []
        for node in lists:
            while node:
                arr.append(node.val)
                node = node.next

        arr.sort()
        dummy = ans = ListNode()
        for i in arr:
            ans.next = ListNode(i)
            ans = ans.next

        return dummy.next