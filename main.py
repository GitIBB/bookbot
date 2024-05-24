import os

def main():
    try:
        print("Current working directory:", os.getcwd())
        print("Opening the file...")
        with open("books/frankenstein.txt") as f:
            print("Reading the file contents...")
            text = f.read()
            print("Printing the file contents...")
            print(text[:400])

            # Count the words in the text
            num_words = count_words(text)
            print("The book contains", num_words, "words")  # This should print 77986 if the text is the whole book

            # Count characters in the text
            char_counts = count_characters(text)

            # Convert dictionary into a list of dictionaries and sort by frequency
            char_counts_list = [{"char": char, "num": count} for char, count in char_counts.items()]
            char_counts_list.sort(reverse=True, key=sorting)

            # Print sorted character counts in a structured manner
            print_report(char_counts_list, num_words)


    except FileNotFoundError:
        print("The file was not found. Please check the file path.")
    except Exception as e:
        print(f"An unexpected error occured: {e}")

def count_words(book_text):
    words = book_text.split()  # Split the text into words
    return len(words)  # Return the number of words

def count_characters(text):
    #lowercase conversion
    lowercase = text.lower()
    chardict = {} #counting dictionary
    for char in lowercase:
        if char.isalpha():
            if char in chardict:
                #increment count if char exists
                chardict[char] += 1
            else:
                #initialize char count
                chardict[char] = 1
    return chardict


# A function that takes a dictionary and returns the value of the num key
def sorting(dict):
    return dict["num"]

def print_report(char_counts_list, num_words):
    print("--- Begin report of frankenstein.txt ---")
    print(f"{num_words} words found")
    #Iterate through the sorted character list and print each character count
    for item in char_counts_list:
        print(f"The '{item['char']} character was found {item['num']} times")
    print(" --- End Report ---")

if __name__ == "__main__":
    print("Starting the main function...")
    main()

