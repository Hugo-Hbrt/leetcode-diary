# Title: Insert into a Binary Search Tree
# Link: https://leetcode.com/problems/insert-into-a-binary-search-tree/
# Difficulty: Medium
# Tags: Tree, Binary Search Tree, Recursion
# Status: Solved
# Date: 2025-07-22

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        elif root.val > val:
            root.left = self.insertIntoBST(root.left, val)

        return root
