def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)


def check_alphabet(word, secret_message):
    sorted_word = sorted(word.lower())
    sorted_secret = sorted(secret_message.lower())
    return sorted_word == sorted_secret


secret_messages = ["haTt", "enPros", "asH", "eMvito"]
word_list_file = "listword.txt"

# Read words from the file into a list
with open(word_list_file, "r") as file:
    word_list = [line.strip() for line in file]

# Sort the word list using quicksort
quicksort(word_list, 0, len(word_list) - 1)

# Find words with the same alphabet as secret messages
matching_words = []
for message in secret_messages:
    for word in word_list:
        if check_alphabet(word, message):
            matching_words.append(word)

# Print the matching words
for word in matching_words:
    print(word)