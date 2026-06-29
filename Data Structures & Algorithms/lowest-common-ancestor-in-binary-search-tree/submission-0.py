# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## optimize later, focus on the solution that's coming


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        common_ancestor = root.val
        if p.val > common_ancestor and q.val > common_ancestor:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p.val < common_ancestor and q.val < common_ancestor:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root