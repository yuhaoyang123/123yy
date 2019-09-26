#递归
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None
        node = root
        node.left,node.right = self.invertTree(node.right),self.invertTree(node.left)
        return node
                    
