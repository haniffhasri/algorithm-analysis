# Read letters from text files
with open('letter1.txt', 'r', encoding='utf-8') as file1, open('letter2.txt', 'r', encoding='utf-8') as file2:
    letter1 = file1.read()
    letter2 = file2.read()

# Split letters into sentences
sentences1 = letter1.split('.')
sentences2 = letter2.split('.')

# Remove empty sentences
sentences1 = [sentence.strip() for sentence in sentences1 if sentence.strip()]
sentences2 = [sentence.strip() for sentence in sentences2 if sentence.strip()]

# Store sentences with different words
different_sentences = []

# Compare sentences and find different words
for i in range(min(len(sentences1), len(sentences2))):
    sentence1 = sentences1[i]
    sentence2 = sentences2[i]

    # Build hash lookup tables for words in each sentence
    lookup_table1 = {word: True for word in sentence1.split()}
    lookup_table2 = {word: True for word in sentence2.split()}

    # Find different words in the sentences
    different_words = []

    for word in lookup_table1:
        if word not in lookup_table2:
            different_words.append(word)

    for word in lookup_table2:
        if word not in lookup_table1:
            different_words.append(word)

    # Check if there are different words in the sentence
    if different_words:
        different_sentences.append((sentence1, sentence2, different_words))

# Print different words for each sentence
for i, (sentence1, sentence2, different_words) in enumerate(different_sentences, start=1):
    print("Sentence {}:".format(i))
    print("Letter 1: {}".format(sentence1))
    print("Letter 2: {}".format(sentence2))
    print("Different words: {}".format(', '.join(different_words)))
    print()