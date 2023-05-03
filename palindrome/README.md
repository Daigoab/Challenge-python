# Challenge-python

# Palindrome

In the code, we use the open() function to open the file words_in_the_english_dictionary.txt in read mode, and then use a for loop to read each line in the file.

For each line in the file, we remove any leading or trailing whitespace using the strip() method, and then check if the word is a palindrome. To check if a word is a palindrome, we compare the word to its reverse using the slicing syntax word[::-1].

If the word is a palindrome, we print it to the console using the print() function.

Note that this code assumes that the file words_in_the_english_dictionary.txt is in the same directory as the Python script. If the file is in a different directory, you will need to provide the full path to the file in the open() function.

The code:

with open ('words_in_english_dictionary.txt', 'r') as file:

    for line in file:

        word = line.strip()

        if word == word[:: -1]:
            print(word)