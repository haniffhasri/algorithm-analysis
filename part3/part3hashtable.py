# Read letters from text files
#running time complexity = O(n1 + n2) where n1 is the amount of words in letter1 and n2 is the amount of words in letter2
with open('letter1.txt', 'r', encoding='utf-8') as file1, open('letter2.txt', 'r', encoding='utf-8') as file2:
    letter1 = file1.read()
    letter2 = file2.read()


def find_unique_words(letter1, letter2):
    words_table1 = {}
    words_table2 = {}

    # Update words_table1 with words from letter1
    for word in letter1.split():
        words_table1[word] = True

    # Update words_table2 with words from letter2
    for word in letter2.split():
        words_table2[word] = True

    # Find unique words in letter1
    unique_words_letter1 = [word for word in words_table1 if word not in words_table2]

    # Find unique words in letter2
    unique_words_letter2 = [word for word in words_table2 if word not in words_table1]

    return unique_words_letter1, unique_words_letter2

unique_words1, unique_words2 = find_unique_words(letter1, letter2)

print("Unique words in letter 1:", unique_words1)
print("Unique words in letter 2:", unique_words2)