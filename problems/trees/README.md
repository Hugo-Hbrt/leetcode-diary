# Problems solved

| Problem | Link | Difficulty |
|---------|------|------------|
| Search in a Binary Search Tree | [https://leetcode.com/problems/search-in-a-binary-search-tree/](https://leetcode.com/problems/search-in-a-binary-search-tree/) | Easy |
| Insert into a Binary Search Tree | [https://leetcode.com/problems/insert-into-a-binary-search-tree/](https://leetcode.com/problems/insert-into-a-binary-search-tree/) | Medium |
| Delete Node in a BST | [https://leetcode.com/problems/delete-node-in-a-bst/](https://leetcode.com/problems/delete-node-in-a-bst/) | Medium |

## Search in a Binary Search Tree

```py

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

```

## Insert into a Binary Search Tree

```py

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

```

## Delete Node in a BST

```py

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
            if (root.left == None):
                if (root.right == None):
                    return None
                else:
                    return root.right
            
            elif (root.right == None):
                return root.left
            
            else:
                min_val = self.findMinNode(root.right).val
                root.right = self.deleteNode(root.right, min_val)
                root.val = min_val

        return root
```
