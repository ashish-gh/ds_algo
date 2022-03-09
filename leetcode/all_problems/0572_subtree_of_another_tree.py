class TreeNode:
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def sub_tree(self, s: TreeNode, t: TreeNode):
        if not t: return True
        if not s: return False

        if self.same_tree(s, t):
            return True
        return (self.sub_tree(s.left, t) or self.sub_tree(s.right, t))
        
    def same_tree(self, s: TreeNode, t: TreeNode):
        if not s and not t: 
            return True

        if (s and t) and (s.val == t.val):
            return (self.same_tree(s.left, t.left) and self.same_tree(s.right, t.right))
        return False
