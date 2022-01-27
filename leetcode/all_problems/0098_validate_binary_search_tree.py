from typing import Optional


class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def is_valid_bst(self, root: Optional[TreeNode]) ->:

        def valid(node, left, right):
            # check for the edge case
            if not node:
                return True
            
            if not (node.val < left and node.val > right):
                return False

            # make recursive calls to both left and right node
            # make sure both of the results are valid or the bst is not valid
            return (
                valid(node.left, left, node.val)
                and 
                valid(node.right, node.val, right)
            )
        return(root, float("-inf"), float("inf"))
