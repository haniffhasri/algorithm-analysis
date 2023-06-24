def binary_search(booklist, target_book):
    low = 0
    high = len(booklist) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_book = booklist[mid].strip()  # Remove leading and trailing spaces

        if mid_book.lower() == target_book.lower():
            print(f"The book '{mid_book}' is found at index {mid}")
            return mid
        elif target_book.lower() < mid_book.lower():
            print(f"The book '{mid_book}' at index {mid}")
            high = mid - 1
        else:
            print(f"The book '{mid_book}' at index {mid}")
            low = mid + 1

    return -1

booklist = [ 'A Study in Scarlet',
            ' Bag of Bones',
            ' Death on the Nile',
            ' Gone With the Wind',
            ' Harry Potter',
            ' Joy Luck Club',
            ' Murder on The Orient Express',
            ' Nemesis',
            ' Pride and Prejudice',
            ' The Book Thief',
            ' The Great Gatsby',
            ' The Kite Runner',
            ' The Lion, the Witch, and the Wardrobe',
            ' The Lord of the Rings',
            ' To Kill a Mockingbird',
            " Winter's Night a Traveler"]

target_book = input("Enter the book title you want to search for: ").lower()

print("Books in the library:", ", ".join(booklist))

result = binary_search(booklist, target_book)
if result != -1:
    print(f"The book '{target_book}' is found at index {result} in the library.")
else:
    print(f"The book '{target_book}' is not found in the library.")
