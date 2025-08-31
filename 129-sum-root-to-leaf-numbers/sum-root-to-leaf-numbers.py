# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        value = 0
        sums = []

        def recuring(root, value, array):
            if not root:
                return
            value = value * 10 + root.val
            if not (root.left or root.right):
                array.append(value)
                return
            
            recuring(root.left, value, array)
            recuring(root.right, value, array)

        recuring(root, value, sums)
        return sum(sums)
