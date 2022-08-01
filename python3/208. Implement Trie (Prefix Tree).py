class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}
        
class Trie:

    def __init__(self):
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        node.is_word = True



    def search(self, word: str) -> bool:
        node = self.root
        for w in word:
            if w not in node.children:
                return False
            node = node.children[w]
        return node.is_word



    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for p in prefix:
            if p not in node.children:
                return False
            node = node.children[p]
        return True
            
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)