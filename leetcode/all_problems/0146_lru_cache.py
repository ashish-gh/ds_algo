class Node:
    def __init__(self, key, val) -> None:
        self.key = key
        self.val = val
        self.next = self.prev = None


class LRUCache:
    def __init__(self, cap: int) -> None:
        self.cap = cap  # to check if we go ovet the capacity
        self.cache = {}  # map key to the nodes

        self.left, self.right = (
            Node(0, 0),
            Node(0, 0),
        )  # dummy nodes to tell where the values are at
        # make some connection to the nodes
        self.left.next = self.right  # to find Least recently used
        self.right.prev = self.left  # to find the most recent used

    # remove node from the list
    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.pre = next, prev

    # insert node at the right
    def insert(self, node):
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node
        node.prev = prev
        node.next = next

    def get(self, key: int):
        if key in self.cache:
            # update the value to the most recent | remove it and add to the right most part
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, val: int):
        if key in self.cache:
            # if the key is already present remove from the list
            self.remove(self.cache[key])
        self.cache[key] = Node(key, val)
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            # remove from the list and delete from the cache or the hash map
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
