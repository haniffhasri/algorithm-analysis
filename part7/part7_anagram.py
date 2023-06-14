def find_anagrams(word, word_list):
    sorted_word = sorted(word.lower())
    anagrams = []

    for w in word_list:
        if sorted(w.lower()) == sorted_word:
            anagrams.append(w)

    return anagrams


secret_message = ['haTt', 'enPros', 'asH', 'eMvito']

# Read word_list from file
with open("listword.txt", "r") as file:
    word_list = file.read().splitlines()

anagrams = []
for message in secret_message:
    message_anagrams = find_anagrams(message, word_list)
    anagrams.extend(message_anagrams)

print("Secret message:")
for anagram in anagrams:
    print(anagram)

