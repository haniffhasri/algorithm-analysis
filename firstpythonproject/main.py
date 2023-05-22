# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

text = "timecomplexityisfunalgorithmisfun"
trie = Trie()
for i in range(len(text)):
    word = ""
    node = trie.root
    for j in range(i, len(text)):
        char = text[j]
        word += char
        if char not in node.children:
            node.children[char] = TrieNode()
        node = node.children[char]
        node.is_end_of_word = True
    trie.insert(word)

def search(trie, word):
    node = trie.root
    for char in word:
        if char not in node.children:
            return False
        node = node.children[char]
    if node is not None and node.is_end_of_word:
        return True
    return False

# search for "algorithm"
if search(trie, "algorithm"):
    print("Found word 'algorithm' in the text")
else:
    print("Word 'algorithm' not found in the text")

# search for "fun"
if search(trie, "fun"):
    print("Found word 'fun' in the text")
else:
    print("Word 'fun' not found in the text")
# Press the green button in the gutter to run the script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
