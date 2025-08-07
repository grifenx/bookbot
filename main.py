import sys
from stats import read_file, count_words, count_chars, sort_chars, construct_message

def main(file_path):
    contents = read_file(file_path)

    num_words = count_words(contents)
    num_chars = sort_chars(count_chars(contents))

    construct_message(num_words, num_chars, file_path)

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main(sys.argv[1])
