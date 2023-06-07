# Read letters from text files
#running time complexity = O(n1 + n2) where n1 is the amount of words in letter1 and n2 is the amount of words in letter2
with open('letter1.txt', 'r', encoding='utf-8') as file1, open('letter2.txt', 'r', encoding='utf-8') as file2:
    letter1 = file1.read()
    letter2 = file2.read()

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key):
        index = self._hash_function(key)
        self.table[index].append(key)

    def search(self, key):
        index = self._hash_function(key)
        for item in self.table[index]:
            if item == key:
                return True
        return False


def build_hash_table(text):
    hash_table = HashTable(10000)  # Choose an appropriate size for your hash table

    words = text.split()
    for word in words:
        hash_table.insert(word)

    return hash_table


def compare_text_files(text1, text2):
    hash_table1 = build_hash_table(text1)
    hash_table2 = build_hash_table(text2)

    unique_words1 = []
    unique_words2 = []

    words1 = text1.split()
    for word in words1:
        if not hash_table2.search(word):
            unique_words1.append(word)

    words2 = text2.split()
    for word in words2:
        if not hash_table1.search(word):
            unique_words2.append(word)

    return unique_words1, unique_words2

unique_words1, unique_words2 = compare_text_files(letter1, letter2)

print("Unique words in letter 1:", unique_words1)
print("Unique words in letter 2:", unique_words2)

