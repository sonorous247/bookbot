def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    letter_counts = count_letters(book_text)
    sorted_letter_dict_list = sort_letter_counts(letter_counts)
    generate_report(book_path,sorted_letter_dict_list,word_count)

def generate_report(path,dict_list,word_count):
    print(f"--- Begin report of {path} ---")
    print(f'{word_count} words found in the document \n')

    for letter_dict in dict_list:
        if letter_dict["letter"].isalpha() :
            print(f"The '{letter_dict["letter"]}' character was found {letter_dict["count"]} times")
    print("--- End report ---")

def sort_letter_counts(letter_dict):

    def sort_on(dict):
        return dict["count"]

    letter_dict_list = []
    for letter in letter_dict:
        letter_dict_list.append({"letter": letter, "count": letter_dict[letter]})
    letter_dict_list.sort(reverse=True, key=sort_on)
    return letter_dict_list

def count_letters(text):
    text_lowered = text.lower()
    letter_count_dict = {}
    for letter in text_lowered:
        if letter in letter_count_dict.keys():
            letter_count_dict[letter] = letter_count_dict[letter]+1
        else:
            letter_count_dict.update({letter: 1})
    return letter_count_dict

def count_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()



if __name__ == "__main__":
    main()