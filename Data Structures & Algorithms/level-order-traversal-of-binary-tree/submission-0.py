# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()

        queue.append(root)
        ans = []

        while queue:
            lvl_len = len(queue)
            lvl = []

            while lvl_len > 0 and queue:
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

                lvl.append(node.val)
                lvl_len -= 1
            ans.append(lvl)
        return ans
