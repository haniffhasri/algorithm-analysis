def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return False

def find_different_words(sentence1, sentence2):
    words1 = sorted(set(sentence1.split()))
    words2 = sorted(set(sentence2.split()))
    different_words = []

    for word in words1:
        if not binary_search(list(words2), word):
            different_words.append(word)

    for word in words2:
        if not binary_search(list(words1), word):
            different_words.append(word)

    return different_words

# Read letters from text files
with open('letter1.txt', 'r', encoding='utf-8') as file1, open('letter2.txt', 'r', encoding='utf-8') as file2:
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
    different_words = find_different_words(sentence1, sentence2)
    if different_words:
        different_sentences.append((sentence1, sentence2, different_words))

# Print different words for each sentence
for i, (sentence1, sentence2, different_words) in enumerate(different_sentences, start=1):
    print("Sentence {}:".format(i))
    print("Letter 1: {}".format(sentence1))
    print("Letter 2: {}".format(sentence2))
    print("Different words: {}".format(', '.join(different_words)))
    print()
