import collections
from typing import Optional


class TreeNode:
    def __init__(self, left, right, val) -> None:
        self.left = left
        self.right = right
        self.val = val


class Solution:
    def level_order_traversal(self, root: Optional[TreeNode]):
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res

