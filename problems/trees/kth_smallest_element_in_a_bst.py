# Title: Kth Smallest Element in a BST
# Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Difficulty: Medium
# Tags: Tree, Depth-first Search, Binary Search Tree
# Status: Solved
# Date: 2025-07-28

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = None 
        i = 0
        
        def inorder(node, i, res):
            nonlocal i, res # To avoid unbound local variable error.
            if not node:
                return
            
            inorder(node.left)
            i += 1
            if i == k:
                res = node.val
            inorder(node.right)
        
        inorder(root)
        return res