class PrefixTree:

    def __init__(self):
        self.root = {}
        self.full = set([])

    def insert(self, word: str) -> None:
        self.innner_insert(word)
        self.full.add(word)
        # print(f"self.root: {self.root}")

    def innner_insert(self, word: str) -> None:
        node = self.root
        for i in range(len(word)):
            if word[i] not in node: node[word[i]] = {}
            node = node[word[i]]

    def search(self, word: str) -> bool:
        return word in self.full

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for i in range(len(prefix)):
            if prefix[i] not in node: return False
            node = node[prefix[i]]
        return True
        