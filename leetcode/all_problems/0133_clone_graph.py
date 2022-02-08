class Node:
    def __init__(self, val, neighbours) -> None:
        self.val = val
        self.neighbours = neighbours


class Solution:
    def clone_graph(self, node: Node) -> Node:
        old_to_new = {}

        def dfs(node):
            if node in old_to_new:
                return old_to_new[node]

            copy = Node(node.val)
            old_to_new[node] = copy
            for neighbour in node.neighbours:
                copy.neighbours.append(dfs(neighbour))
            return copy

        return dfs(node) if node else None

