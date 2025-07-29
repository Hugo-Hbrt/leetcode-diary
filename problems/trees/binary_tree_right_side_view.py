# Title: Binary Tree Right Side View
# Link: https://leetcode.com/problems/binary-tree-right-side-view/
# Difficulty: Medium
# Tags: Tree, Depth-first Search, Breadth-first Search
# Status: Solved
# Date: 2025-07-29

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        queue = []
        queue.append(root)
        
        while len(queue) > 0:
            n = len(queue)
            for i in range(n):
                node = queue.pop(0)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                if i == n-1:
                    res.append(node.val)
        
        return res