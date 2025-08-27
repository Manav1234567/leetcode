"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        q = []
        q.append([root, 0])

        pos = 0
        result = []
        result.append([root])

        while q:
            node, level = q.pop(0)
            pos = level + 1
            if (node.left or node.right) and pos == len(result):
                result.append([])
            if node.left:
                q.append([node.left, pos])
                result[pos].append(node.left)
            if node.right:
                q.append([node.right, pos])
                result[pos].append(node.right)

        for i in result:
            for j in range(len(i)):
                if j < len(i) - 1:
                    i[j].next = i[j+1]

        return root