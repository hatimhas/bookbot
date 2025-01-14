def main ():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()
        num_words = calculate_words(file_contents.split())
        
        char_num = calc_char(file_contents)
        
        create_report(char_num, book_path, num_words)

def calculate_words (words):
    return len(words)

def calc_char(text):
    char_dict = {}
    for char in text:
        low_char = char.lower()
        if low_char not in char_dict:
            char_dict[low_char] = 1
        else:
            char_dict[low_char] +=1
    return char_dict
# Makes Dict able to be .sort
def create_report(dict,book,num_words):
    dict_to_list = list(dict.items())
    sorted_list = sorted(dict_to_list, key=lambda x:x[1], reverse=True)
    
    print(f"--- Begin report of {book} ---")
    print(f"{num_words} words found in the document")
    print("")
    for char in sorted_list:
        if not char[0].isalpha():
            continue
        print(f"The '{char[0]}' was found {char[1]}")
    
    print("--- End report ---")

    
   
        

main()

# list = [('a', 1), ('b', 2), ('c', 3)]
# for char in list:
#     print(char[0], char[1])