# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        state = [k, None]
        # DFS Algo
        def dfs_inorder(root):
            if not root or state[1] is not None:
                return 

            # Visit Left Nodes
            dfs_inorder(root.left)

            # Process Current Nodes
            state[0] -= 1
            if state[0] == 0:
                state[1] = root.val
                return 

            dfs_inorder(root.right)

        dfs_inorder(root)
        return state[1]



            

            

            







            

            