Algorithm :
1. Iporting libraries:
   1. importing re , symspellpy , nltk and spacy
   2. loading corpus of english words
   3. also loading the dictionary for symspellpy (added the dictionary here as well)
2. defining correct_word function
   1. if a word exists in nltk words corpus return the word
   2. else , search the closest word using symspellpy
   3. if word is found , restore its case and return
   4. return the word if none of the case matches
3. defining restore_capital function
   1. if original word is titlecase , return new word in title case
   2. if original word is uppercase , return uppercase new word
   3. if original is lowercase , return new word in lowercase
4. defining restore_sentence function
   1. using re library to split words and other characters
   2. if it is a word pass through correct_word
   3. else punctuation add as it is
   4. return reassembled correct sentence
5. defining get_nouns
   1. using spacy library to return a sorted list of nouns using NER
6. defining get_comma
   1. using re library to find "However" in sentence if it is not followed by comma add one and return the sentence
7. the test_cases is a list of all test cases given
8. iterate through each element of list , first restore sentence , get nouns and last get commas and print corrected 
