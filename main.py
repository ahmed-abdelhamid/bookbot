import sys
from stats import count_words, count_letters, generate_list

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_content = get_book_text(book_path)
    word_count = count_words(book_content)
    letters_count = count_letters(book_content)
    letters_list = generate_list(letters_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for letter in letters_list:
        if not letter['char'].isalpha():
            continue # skip non-alphabetic characters
        print(f"{letter['char']}: {letter['num']}")
    print("============= END ===============")

main()