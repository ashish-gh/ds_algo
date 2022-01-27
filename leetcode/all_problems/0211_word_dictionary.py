class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.end_of_word = False


class WordDictionary:
    def __init__(self) -> None:
        self.root = TrieNode()

    def add_word(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end_of_node = True

    def search(self, word):
        def dfs(j, root):
            cur = root
            # we want to make sure we always don't want to start at the index position,
            # so we have to define from where we want to start
            for i in range(j, len(word)):
                c = word[i]
                # above character could be any character from a-z or could be .
                if c == ".":
                    # if the character is . , we will potentially be going down the path for 26 times
                    # we will use backtracking or recursing to track the algorithms
                    for child in cur.children.values():
                        # we will be basically going down the child so we will have to pass (i +1)
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    # lets check if the character exists or not
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.end_of_word

        return dfs(0, self.root)
