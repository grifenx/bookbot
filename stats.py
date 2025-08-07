def read_file(file_path):

    with open(file_path) as f:
        contents = f.read()

    return contents

def count_words(contents):
    return len(contents.split())

def count_chars(contents):
    char_dict = {}

    for char in contents.lower():
        if char not in char_dict and char.isalpha():
            char_dict[char] = 1
        elif char.isalpha():
            char_dict[char] +=1
        else:
            continue

    return char_dict

def sort_on(items):
    return items["num"]

def sort_chars(char_dict):
    char_list_dict =  [{"char": k, "num": v} for k, v in char_dict.items()]
    char_list_dict.sort(reverse=True, key=sort_on)

    return char_list_dict

def construct_message(words_count, chars_count, file_path):
    formatted_char_str = []
    for item in chars_count:
        formatted_char_str.append(f"{item['char']}: {item['num']}")
    char_string = "\n".join(formatted_char_str)
    
    message_str = f"""
============ BOOKBOT ============
Analyzing book found at {file_path}...
----------- Word Count ----------
Found {words_count} total words
--------- Character Count -------
{char_string}
============= END ===============
    """
    
    print(message_str)