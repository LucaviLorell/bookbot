def get_num_words(booktext):
  return len(booktext.split())

def get_num_char(booktext):
  char_dict = {}
  for i in range(0,len(booktext)):
    current_char = booktext[i].lower()
    if current_char not in char_dict:
      char_dict[current_char] = 0
    char_dict[current_char] += 1
  return char_dict

def get_book_text(filepath):
  with open(filepath) as book:
    booktext = book.read()
    return booktext

def sort_on(items):
  return items["num"]

def sort_dicts(char_dict):
  combined_list =[]
  for entry in char_dict:
    temp_dict = {}
    temp_dict["char"] = entry
    temp_dict["num"] = char_dict[entry]
    # print(f"this is the current temp_dict {temp_dict}")
    combined_list.append(temp_dict)
    # print(f"this is the current combined_list {combined_list}")
  combined_list.sort(reverse=True, key=sort_on)
  # print(f"this is the sorted list, {sorted_list}")
  return combined_list