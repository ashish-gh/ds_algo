class NodeTire:
    def __init__(self) -> None:
        self.children = []
        self.end_of_word = False


class Trie:
    def __init__(self) -> None:
        self.root = NodeTire()

    def insert(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = NodeTire()
            cur = cur.children[c]
        cur.end_of_word = True

    def search(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.end_of_word

    def starts_with(self, preifx):
        cur = self.root
        for c in preifx:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True

