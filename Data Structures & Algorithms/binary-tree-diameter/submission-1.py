# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        longest_diameter_so_far = 0

        def dfs(root):
            """
            It's Depth First Search (DFS)

            recursively checking left and right nodes
            if nothing exists recursive step returns 0 to add
            if something exists 
            recursive step returns 1 to add for itself
            plus max of its left and right children height
            -- if no children it will return 0
            -- any children will do the same recursive function
            post order dfs
            """
            nonlocal longest_diameter_so_far

            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            longest_diameter_so_far = max(longest_diameter_so_far, left + right)


            return 1 + max(left, right)

        dfs(root)
        return longest_diameter_so_far