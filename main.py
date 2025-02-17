def word_count(text):
    return len(text.split())


def num_of_each_char(text):#creates a dictionary that shows how many of each character there is
    lower_text = text.lower()
    char_counts = {}

    for char in lower_text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_on(dict):
    #helper function for sorting
    return dict["num"]

def convert_to_list(char_counts):
    char_list = []
    for char, count in char_counts.items():
        if char.isalpha():
            char_dict = {"char": char, "num": count}
            char_list.append(char_dict)
    char_list.sort(reverse=True, key=sort_on)
    return char_list


def main():
    with open("books/Frankenstein.txt") as f: #opens the Frankenstein book
        file_contents = f.read()  #reads the contents into a string

    print("--- Begin report of books/Frankenstein.txt ---")
    count = word_count(file_contents)
    print(f"{count} words found in the document\n")#\n for empty line

    letters = num_of_each_char(file_contents)
    char_list = convert_to_list(letters)
    #loop through char_list
    for char_dict in char_list:
        print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")
    
    print("--- End report ---")

main()


