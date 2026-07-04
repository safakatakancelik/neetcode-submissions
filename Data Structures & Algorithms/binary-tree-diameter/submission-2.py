# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # initialize a variable to use during checks
        longest_diameter_so_far = 0

        # post order Depth First Search (DFS)
        def dfs(root): 
            nonlocal longest_diameter_so_far # give the nested function access to this nonlocal variable

            if not root: # return 0 if nothing exists, no edge here
                return 0

            # recurse through each child node, traverse the entire tree
            left = dfs(root.left)
            right = dfs(root.right)

            # calculate the current diameter 
            diameter_from_the_current_node = left + right

            # check if the current diameter is the longest we have found, update if so
            longest_diameter_so_far = max(longest_diameter_so_far, diameter_from_the_current_node)

            # return level/edge count i.e depth
            return 1 + max(left, right)
            ## 1 for the current node to its parent
            ## + depth of the deepest child tree

        # start the DFS
        dfs(root)

        # return the longest diameter in this binary tree
        return longest_diameter_so_far