from check_input import check_input
def task4():
    #Get sting and count words that conains only 3 letters
    def count_three_letter_words(input_string):
        cleaned_string = ''.join(c for c in input_string if c.isalnum() or c.isspace())
        words = cleaned_string.split()  # Split the cleaned string into words
        three_letter_words = [word for word in words if len(word) == 3]  # Filter words with length 3
        return len(three_letter_words)
    
    # Check if in word the same amount of vowels and consonants
    def count_vowels_and_consonants(word):
        vowels = "aeiouAEIOU"
        consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    
        num_vowels = sum(1 for char in word if char in vowels)
        num_consonants = sum(1 for char in word if char in consonants)

        if num_vowels == num_consonants:
            return True
        return False

    #Get string and find words that include the same amount of vowels and consonants, return list of that words and their position
    def find_words_with_equal_vowels_and_consonants(input_string):
        # cleaned_string = ''.join(c for c in input_string if c.isalpha() or c.isspace())
        rawwords = input_string.split()
        words = [word for word in rawwords if word.isalpha()]
        result = []
    
        for i, word in enumerate(words):
            #check = count_vowels_and_consonants(word)
            if count_vowels_and_consonants(word):
                result.append((word, i + 1))
    
        return result
    
    # Get string, and return words in descending order
    def in_descending_order(input_string):
        cleaned_string = ''.join(c for c in input_string if c.isalnum() or c.isspace())
        words = cleaned_string.split()
        result = []
        for i, word in enumerate(words):
            result.append((len(word), word))
        result.sort(reverse=True)
        return result
        



    print("Enter your string:")
    res = check_input(str,  "NO VALUE")
    amount = count_three_letter_words(res)
    print(f"Amount of three letter words: {amount}")
    matching_words = find_words_with_equal_vowels_and_consonants(res)
    for word, position in matching_words:
        print(f"Word: {word}, Position: {position}")
    word_list = in_descending_order(res)
    for length, word in word_list:
        print(f"Word: {word}, Length: {length}")

#task4()
    