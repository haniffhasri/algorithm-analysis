class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def __iter__(self):
        return self._generate_words(self.root, "")

    def _generate_words(self, node, prefix):
        if node.is_end_of_word:
            yield prefix
        for char, child in node.children.items():
            yield from self._generate_words(child, prefix + char)


def check_alphabet(word, secret_message):
    sorted_word = sorted(word.lower())
    sorted_secret = sorted(secret_message.lower())
    return sorted_word == sorted_secret


secret_messages = ["haTt", "enPros", "asH", "eMvito"]
word_list_file = "listword.txt"

# Read words from the file and insert them into a Trie
word_trie = Trie()
with open(word_list_file, "r") as file:
    for line in file:
        word = line.strip()
        word_trie.insert(word.lower())

# Find words with the same alphabet as secret messages
matching_words = []
for message in secret_messages:
    for word in word_trie:
        if check_alphabet(word, message):
            matching_words.append(word)

# Print the matching words
for word in matching_words:
    print(word)