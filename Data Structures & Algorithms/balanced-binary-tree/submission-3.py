# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # variable to track if it's height balanced
        is_height_balanced = True
        
        # recursive function depth first search
        def dfs(root):
            # accessing our variable
            nonlocal is_height_balanced
            
            # if imbalance is found, just keep returning
            if not is_height_balanced:
                return 0
            
            # handle non existent root case
            ## if a node doesn't exist, there's nothing to count
            if not root:
                return 0

            # recurse towards left and right nodes
            left = dfs(root.left)
            right = dfs(root.right)
            
            # check if the current node is imbalanced
            if (abs(left - right) > 1):
                is_height_balanced = False

            # return the height of the current node
            return 1 + max(left, right)

        # start the search
        dfs(root)
        return is_height_balanced
