# Title: Construct Binary Tree from Preorder and Inorder Traversal
# Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# Difficulty: Medium
# Tags: Tree, Depth-first Search, Binary Tree, Array
# Status: Solved
# Date: 2025-07-29

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indexes = dict()
        for i, num in enumerate(inorder):
            indexes[num] = i
        
        pre_idx = 0
        
        def dfs(l, r):
            nonlocal pre_idx
            if l > r:
                return None
            
            val = preorder[pre_idx]
            root = TreeNode(val)
            pre_idx += 1
            mid = indexes[val]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)

            return root
        
        return dfs(0, len(preorder) - 1)