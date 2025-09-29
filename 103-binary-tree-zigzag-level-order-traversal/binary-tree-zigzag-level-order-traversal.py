# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        queue = collections.deque([root])
        res = []
        leftToRight = True

        while queue:

            level = []
            for _ in range(len(queue)):

                node = queue.popleft()

                level.append(node.val)
                queue.append(node.left) if node.left else None
                queue.append(node.right) if node.right else None

            if leftToRight:
                res.append(level)
            else:
                res.append(level[::-1])

            leftToRight = not leftToRight

        return res
                