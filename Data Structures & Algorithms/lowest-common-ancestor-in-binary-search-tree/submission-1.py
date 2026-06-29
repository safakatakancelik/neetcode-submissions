# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        current_node = root
        while current_node:
            if p.val > current_node.val and q.val > current_node.val:
                current_node = current_node.right
            elif p.val < current_node.val and q.val < current_node.val:
                current_node = current_node.left
            else:
                return current_node