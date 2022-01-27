import collections
from tkinter.tix import Tree
from typing import Optional
from xml.dom.minicompat import NodeList

# Three ways to implement this
# 1. Breadth First Search | Level order traversal


class Node:
    def __init__(self, left, right, value) -> None:
        self.left = left
        self.right = right
        self.value = value


class Solution1:
    def max_depth(self, root: Optional[Node]):
        level = 0
        q = collections.deque()

        q.append(root)
        while q:
            level_found = False
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    level_found = True
                    q.append(node.left)
                    q.append(node.right)
            if level_found:
                level += 1
        return level


# Depth First Search | Recursive-Iterative Approach


class Solution1:
    def max_depth(self, root: Optional[Node]):
        if not root:
            return 0

        return 1 + max(self.max_depth(root.left), self.max_depth(root.right))


class Solution2:
    def max_depth(self, root: Optional[Node]):
        stack = [[root, 1]]
        res = 0
        while stack:
            node, level = stack.pop()
            if node:
                res = max(res, level)
                stack.append([node.left, level + 1])
                stack.append([node.right, level + 1])
        return res

        ...
