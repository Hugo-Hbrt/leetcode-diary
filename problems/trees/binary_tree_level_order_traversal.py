# Title: Binary Tree Level Order Traversal
# Link: https://leetcode.com/problems/binary-tree-level-order-traversal/
# Difficulty: Medium
# Tags: Tree, Breadth-first Search
# Status: Solved
# Date: 2025-07-29

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = []

        queue.append(root)

        while len(queue) > 0:
            layer = []
            for i in range(len(queue)):
                
                node = queue.pop(0)
                layer.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            res.append(layer)
        
        return res
