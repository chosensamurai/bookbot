def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = character_count(text)
    sort = sort_on(char_count)
    print(f"---Begin report of {book_path} ---")
    print(f"{num_words} words found here {book_path}")
    for char, count in sort:
        print(f"The {char}: was found {count} times")
    print (f"--- End Report ---")
    #print ("charcount",char_count)
    
def get_book_text(path):
    with open(path) as f:
        return f.read()
def get_num_words(text):
    words = text.split()
    return len(words)
def character_count(text):
    char_count = {}
    lower_case_text = text.lower()
    for character in lower_case_text:
        if character in char_count:
            char_count[character] +=1
            #print (f"adding {character}")
        else:
            char_count[character] =1
            #print(f"skipping {character}")
    return char_count

def sort_on(dictionary):
    # Use sorted() on dictionary.items()
    sorted_items = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)  # Sort by values (descending)
    return sorted_items

        

main()
