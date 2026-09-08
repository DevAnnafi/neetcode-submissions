# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        queue = deque([root])

        while queue:
            node = queue.popleft()
            # Swap the children
            node.left, node.right = node.right, node.left

            # Add children to the queue for processing in the next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root
        


