# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        value = 0
        sums = []

        def recuring(root, value, array):
            if not root:
                return
            value += root.val
            if not (root.left or root.right):
                array.append(value)
                return
            
            recuring(root.left, value, array)
            recuring(root.right, value, array)

        recuring(root, value, sums)
        return (targetSum in sums)
        