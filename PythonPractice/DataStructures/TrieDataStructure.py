# Python Program for insert and search operation in a Trie


class TrieNode:
    # Trie Node Class
    def __init__(self):
        self.children = [None]*26
        # isEndOfWord is True if the node represents the end of the word
        self.isEndOfWord = False

class Trie:
    # Trie data Structure Class
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        # Returns the new Trie Node
        return TrieNode()

    def _charToIndex(self, ch) :
        # Converts the given character to alphabets
        return ord(ch) - ord('a')

    def insert(self, key):

        pcrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pcrawl.children[index]:
                pcrawl.children[index] = self.getNode()
            pcrawl = pcrawl.children[index]
        pcrawl.isEndOfWord = True

    def search(self, key):

        pcrawl = self.root
        length = len(key)

        for level in range(length):
            index = self._charToIndex(key[level])
            if not pcrawl.children[index]:
                return False
            pcrawl = pcrawl.children[index]

        return pcrawl != None and pcrawl.isEndOfWord

# Test Stub
def main():

    n = int(input())
    o_n = int(input())

    keys = list(input().strip().split())[:n]
    output = ["Not present in trie", "Present in trie"]
    search_string = list(input().strip().split())[:o_n]
    # Initialize the Trie
    t = Trie()

    # Construct the Trie
    for key in keys:
        t.insert(key)

    # Search for different keys
    for s_string in search_string:
        print("{} ---- {}".format(s_string, output[t.search(s_string)]))


if __name__ == '__main__':
    main()