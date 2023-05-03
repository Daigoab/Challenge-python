with open ('words_in_english_dictionary.txt', 'r') as file:

    for line in file:

        word = line.strip()

        if word == word[:: -1]:
            print(word)