class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def serialize(self, root):
        res = []

        def dfs(node):
            if node is None:
                res.append("N")
                return
            res.append(str(node.data))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)

