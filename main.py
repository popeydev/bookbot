def main():
    global book_path, text, num_words, num_letters, results, result_dict
    book_path = "books/frankenstein.txt"                                    #this is where the input file is located
    text = get_book_text(book_path)                                         #reads the input file
    num_words = get_num_words(text)                                         #works out word count
    num_letters, letters_main_dict = get_num_letters(text)                  #returns the number of letters, and a dictionary include the count of each letter
    result_dict = [{'letter': key, 'number': value} for key, value in letters_main_dict.items()] #puts the dictionary with the counts into a list and gives it "letter" and "number" keys

    report(text)

def get_num_words(text):  #used to determine word count
    words = text.split()
    return len(words)

def get_num_letters(text):   #used to determine letter count, and add num letters to a dict
    letters = text.lower()
    letters_dict = {}
    for x in letters:
        if x not in letters_dict:
            letters_dict[x] = 1
        else:
            letters_dict[x] += 1
    return letters_dict, letters_dict

def get_book_text(path):          #reads the text from the input file
    with open(path) as f:
        return f.read()

def sorted_lists(input):          #sorts the input based on the number of times each 'number' appears descending
    sorted_list = sorted(input, reverse=True, key=lambda d: d['number'])
    return sorted_list

def report(text):                #generates a report with word count and a list of how often each letter appears.
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    for x in sorted_lists(result_dict):
        letter = x['letter']
        number = x['number']
        print(f"The '{letter}' character was found {number} times")
    print(f"--- End report ---")

main()