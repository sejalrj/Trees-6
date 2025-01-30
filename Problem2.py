# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Idea over here is to use column to be able to rack off vertical orders as well as row levels as we want to arrange elements in same vertical line in sorted order

        TC and SC : 

        For BFS -> O(N), O(N)
        For DFS -> O(N*KlogK), O(N)
        """
        if not root:
            return []
        levels = defaultdict(list)
        q = collections.deque()
        q.append((root, 0))
        
        while q:
            cur, level = q.popleft()
            
            levels[level].append(cur.val)

            if cur.left:
                q.append((cur.left, level-1))
            if cur.right:
                q.append((cur.right, level+1))

        
        res= [levels[i] for i in range(min(levels), max(levels)+1)]

        return res

        """
        DFS"""

        
        hashmap = defaultdict(list)

        def helper(root, level, row):
            if not root:
                return
            
            hashmap[level].append((row, root.val))
            helper(root.left, level-1 ,row+1)
            helper(root.right, level+1, row+1)
            return
        
        helper(root, 0, 0)
        res = []
        minn, maxx = min(hashmap.keys()), max(hashmap.keys())
        for i in range(minn, maxx+1):
            temp = sorted(hashmap[i], key= lambda x:(x[0], x[1]))
            temp = [j for i,j in temp]
            res.append(temp)
        return res
            
        
