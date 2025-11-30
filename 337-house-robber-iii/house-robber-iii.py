# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            # base case: if we reach the leaves, return the same number
            if not node:
                return (0, 0)

            # recursive: rob or not rob
            # if we rob the left subtree
            left_rob, left_not = dfs(node.left)
            right_rob, right_not = dfs(node.right)

            # if we rob this node
            rob_this = node.val + left_not + right_not
            not_rob = max(left_rob, left_not) + max(right_rob, right_not)

            return (rob_this, not_rob)

        rob_this, not_rob = dfs(root)
        return max(rob_this, not_rob)