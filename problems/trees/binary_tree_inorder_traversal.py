# Title: Binary Tree Inorder Traversal
# Link: https://leetcode.com/problems/binary-tree-inorder-traversal/
# Difficulty: Easy
# Tags: Tree, Depth-first Search 
# Status: Solved
# Date: 2025-07-28

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        
        inorder(root)
        return res