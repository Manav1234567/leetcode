# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        queue = []

        def makeQueue(root, queue):
            if not root:
                return
            queue.append(root)
            makeQueue(root.left, queue)
            makeQueue(root.right, queue)

        makeQueue(root, queue)
        curr = queue.pop(0)
        curr.left = None
        curr.right = None
        while queue:
            node = queue.pop(0)
            node.left = None
            node.right = None
            curr.right = node
            curr = curr.right
        return root
            