# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
Idea for serialize is to traverse the tree by level order and put it in the list of strings that would be sent to  derealize, in desrealize I am using 2 pointers, i is to keep track of the current node and j is to keep track of its child's 

TC for both methods - O(N)
SC for both methods - O(N)
"""
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        q = deque([root])
        
        serialized_tree = []
        while q:
            cur = q.popleft()
            if cur != None:
                serialized_tree.append(str(cur.val))

                q.append(cur.left)
                q.append(cur.right)
            else:
                serialized_tree.append("None")

        # print(serialized_tree)
        return ",".join(serialized_tree)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(",")
        print(data)
        nodes = [TreeNode(int(i)) if i!= 'None' else None for i in data]
        # print(nodes)
        i = 0 #for moving roots
        j = 1 #for subroots
        #['1', '2', '3', 'None', 'None', '4', '5', 'None', 'None', 'None', 'None']
        while i < len(nodes):
            if nodes[i] != None:
                if j < len(nodes):
                    nodes[i].left = nodes[j]
                    j += 1
                if j < len(nodes):
                    nodes[i].right = nodes[j]
                    j+=1
            i += 1
            
        # print(nodes[0])
        return nodes[0]

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
