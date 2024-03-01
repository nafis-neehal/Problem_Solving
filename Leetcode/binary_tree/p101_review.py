# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check_mirror_image(root1, root2):
            
            if root1==None and root2==None:
                return True
            
            if (root1 and not root2) or (root2 and not root1):
                return False
            
            if root1.val==root2.val:
                return check_mirror_image(root1.left, root2.right) and check_mirror_image(root1.right, root2.left)

        return check_mirror_image(root, root)

        
        