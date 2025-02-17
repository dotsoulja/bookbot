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


def main():
    with open("books/Frankenstein.txt") as f: #opens the Frankenstein book
        file_contents = f.read()  #reads the contents into a string
    count = word_count(file_contents)
    print(f"The book contains {count} words")

    letters = num_of_each_char(file_contents)
    print("the breakdown of how many of each character are as follows:")
    for char, in sorted(letters.keys()):#prints each key and value on seperate line alphabetically
        print(f"'{char}': {letters[char]}")

main()


