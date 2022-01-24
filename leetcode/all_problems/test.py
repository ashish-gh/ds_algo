class Node:
    def __init__(self, key, val) -> None:
        self.key = key
        self.val = val
        self.next = self.prev = None


class LRUCache:
    def __init__(self, cap) -> None:
        self.cap = cap
        self.cache = {}

        # empty node
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def insert(self, node):
        ...

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def get(self, key):
        if key in self.cache:
            # remove from the previous and insert at the end
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key]
        return -1

    def put(self, key, val):
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, val)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[key].val

