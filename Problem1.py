# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        """
        using int based recursion

        TC and SC : O(N) and O(N)
        """
   
        def helper(root):
            if not root:
                return 0
            summ = 0
            if low <= root.val <= high: summ += root.val
            if root.val >= low:
                summ += helper(root.left)
            if root.val <= high:
                summ += helper(root.right)
            return summ
        
        return helper(root)
        
        
        """
        using void based recursion
        """
        summ = 0
        def helper(root): 
            nonlocal summ
            if not root:
                return
            
            if low <= root.val <= high: summ += root.val
            if root.left.val >= low:
                helper(root.left)
            if root.val <= high:
                helper(root.right)
            return
        helper(root)
        return summ
        
