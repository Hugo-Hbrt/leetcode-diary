# Problems solved

| Problem | Link | Difficulty |
|---------|------|------------|
| Construct Binary Tree from Preorder and Inorder Traversal | [https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | Medium |
| Search in a Binary Search Tree | [https://leetcode.com/problems/search-in-a-binary-search-tree/](https://leetcode.com/problems/search-in-a-binary-search-tree/) | Easy |
| Insert into a Binary Search Tree | [https://leetcode.com/problems/insert-into-a-binary-search-tree/](https://leetcode.com/problems/insert-into-a-binary-search-tree/) | Medium |
| Binary Tree Level Order Traversal | [https://leetcode.com/problems/binary-tree-level-order-traversal/](https://leetcode.com/problems/binary-tree-level-order-traversal/) | Medium |
| Delete Node in a BST | [https://leetcode.com/problems/delete-node-in-a-bst/](https://leetcode.com/problems/delete-node-in-a-bst/) | Medium |
| Kth Smallest Element in a BST | [https://leetcode.com/problems/kth-smallest-element-in-a-bst/](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | Medium |
| Binary Tree Inorder Traversal | [https://leetcode.com/problems/binary-tree-inorder-traversal/](https://leetcode.com/problems/binary-tree-inorder-traversal/) | Easy |

## Construct Binary Tree from Preorder and Inorder Traversal

```py

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
```

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

## Binary Tree Level Order Traversal

```py

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

## Kth Smallest Element in a BST

```py

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
```

## Binary Tree Inorder Traversal

```py

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
```
