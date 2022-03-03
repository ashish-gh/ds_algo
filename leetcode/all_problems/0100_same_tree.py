class NodeTree:
    def __init__(self, val= 0, left = None, right = None) -> None:
        self.val = val
        self.left = left 
        self.right = right 


class Solution:
    def same_tree(self, p: NodeTree, q: NodeTree) -> bool:

        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        
        return (self.same_tree(p.left, q.left) and self.same_tree(p.right, q.right))
        
