# Title: Search in a Binary Search Tree
# Link: https://leetcode.com/problems/search-in-a-binary-search-tree/
# Difficulty: Easy
# Tags: Binary Search Tree, Tree
# Status: Solved
# Date: 2025-07-16

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val > val:
            return self.searchBST(root.left, val)
        elif root.val < val:
            return self.searchBST(root.right, val)
        else:
            return root
