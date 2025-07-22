# Title: Delete Node in a BST
# Link: https://leetcode.com/problems/delete-node-in-a-bst/
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
    def findMinNode(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        current = root
        while current and current.left:
            current = current.left
        
        return current
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        
        else:
            # Case 0/1
            if (root.left == None):
                if (root.right == None):
                    return None
                else:
                    return root.right
            
            elif (root.right == None):
                return root.left
            
            # Case 2
            else:
                # Find min value in right subtree
                min_val = self.findMinNode(root.right).val
                # Remove min value in right subtree
                root.right = self.deleteNode(root.right, min_val)
                # Replace value with min
                root.val = min_val

        return root