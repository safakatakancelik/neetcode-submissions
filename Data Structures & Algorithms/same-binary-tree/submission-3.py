# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if both are null, it's a match
        if not p and not q:
            return True
        
        # if both exists and values are equal, go deeper
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        ## we are left with scenarios:
        ### 1. both exists and values are not equal
        ### 2. only one exists and therefore they are not equal
        else:
            return False
