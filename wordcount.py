def count_words(string):
    words = string.split()
    return len(words)

string = input("Enter a string: ")
word_count = count_words(string)
print(f"The number of words in the string is: {word_count}")
