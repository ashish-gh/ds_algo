

from typing import Optional


class TreeNode:
    def __init__(self,val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invert_binary_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # check for base case
        if not root:
            return None
        
        # swap the positions of the tree node
        tmp = root.left
        root.left = root.right
        root.right = tmp

        # invert trees on both left and right side
        self.invert_binary_tree(root.left)
        self.invert_binary_tree(root.right)

        return root

        

