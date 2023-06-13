from collections import deque

def generate_adjacent_words(word):
    """
    Generate all words that can be formed by changing exactly two letters in the given word.
    """
    adjacent_words = []
    word_length = len(word)
    
    for i in range(word_length):
        for j in range(i + 1, word_length):
            adjacent_word = list(word)
            adjacent_word[i], adjacent_word[j] = adjacent_word[j], adjacent_word[i]
            adjacent_words.append(''.join(adjacent_word))
    
    return adjacent_words

def bfs_find_different_words(sentence1, sentence2):
    words1 = set(sentence1.split())
    words2 = set(sentence2.split())
    different_words = []

    graph = {}
    visited = set()

    # Create graph
    for word in words1 | words2:
        graph[word] = set(generate_adjacent_words(word))

    # Perform BFS
    queue = deque()

    for word in words1:
        queue.append(word)
        visited.add(word)

    while queue:
        current_word = queue.popleft()

        if current_word in words2:
            different_words.append(current_word)

        if current_word not in graph:
            print("Word '{}' not found in the graph".format(current_word))
            continue

        adjacent_words = graph[current_word]
        for adjacent_word in adjacent_words:
            if adjacent_word not in visited:
                queue.append(adjacent_word)
                visited.add(adjacent_word)

    return different_words

# Read letters from text files
with open('C:/Users/hp/Documents/GitHub/algorithm-analysis/part3/letter1.txt', 'r', encoding='utf-8') as file1, open('C:/Users/hp/Documents/GitHub/algorithm-analysis/part3/letter2.txt', 'r', encoding='utf-8') as file2:
    letter1 = file1.read()
    letter2 = file2.read()


sentences1 = letter1.split('.')
sentences2 = letter2.split('.')

# Remove empty sentences
sentences1 = [sentence.strip() for sentence in sentences1 if sentence.strip()]
sentences2 = [sentence.strip() for sentence in sentences2 if sentence.strip()]

# Find different words for each sentence
different_sentences = []
for i in range(min(len(sentences1), len(sentences2))):
    sentence1 = sentences1[i]
    sentence2 = sentences2[i]
    different_words = bfs_find_different_words(sentence1, sentence2)
    if different_words:
        different_sentences.append((sentence1, sentence2, different_words))

# Print different words for each sentence
for i, (sentence1, sentence2, different_words) in enumerate(different_sentences, start=1):
    print("Sentence {}:".format(i))
    print("Letter 1: {}".format(sentence1))
    print("Letter 2: {}".format(sentence2))
    print("Different words: {}".format(', '.join(different_words)))
    print()
