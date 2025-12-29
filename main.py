from stats import get_book_text, get_num_words, get_num_char, sort_dicts
import sys

def check_args():
  if len(sys.argv) ==2:
    return
  print("Usage: python3 main.py <path_to_book>")
  sys.exit(1)

check_args()

def print_report(book_location, num_words, dictionary_list):
  print(f"============ BOOKBOT ============\nAnalyzing book found at {book_location}...\n----------- Word Count ----------\nFound {num_words} total words\n--------- Character Count -------")
  for dictionary in dictionary_list:
    if dictionary["char"].isalpha():
      print(f"{dictionary["char"]}: {dictionary["num"]}")
  print("============= END ===============")

book_location = sys.argv[1]
booktext = get_book_text(book_location)
num_words = get_num_words(booktext)
char_dict = get_num_char(booktext)
sorted_list = sort_dicts(char_dict)

def main():
  print_report(book_location, num_words, sorted_list)

main()
