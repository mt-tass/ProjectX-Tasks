import re
#from symspellpy import SymSpell
import nltk
from nltk.corpus import words
import spacy
import os
def get_dictionary(path):
	with open(path,'r') as file:
		return set(word.strip().lower() for word in file)

eng_dict = get_dictionary("eng_dictionary.txt")
nlp = spacy.load("en_core_web_sm")

#sym_spell = SymSpell(max_dictionary_edit_distance=1)
#sym_spell.load_dictionary("en-80k.txt", term_index=0, count_index=1)
error_map = {
    '5':'s',
    'e':'c',
    'c':'e'
}

def correct_error(word):
    word = list(word)
    for i,char in enumerate(word):
        if char in error_map:
            og_char = word[i]
            word[i] = error_map[char]
            new_word = ''.join(word)
            if new_word.lower() in eng_dict:
                return new_word
            word[i] = og_char
    return ''.join(word)
def correct_word(word):
    raw = word
    lower = word.lower()
    
    if lower in eng_dict:
        return word 
    new_word = correct_error(word)
    #print(new_word)
    if new_word.lower() in eng_dict :
        return restore_case(word,new_word)
    else:
        return word
def restore_case(og, corrected):
    if og.istitle():
        return corrected.capitalize()
    elif og.isupper():
        return corrected.upper()
    else:
        return corrected

def restore_sentence(text):
    restored = []
    for word in re.findall(r'\w+|\W+', text):
        if word.strip() and any(c.isalpha() for c in word):
            restored.append(correct_word(word))
        else:
            restored.append(word)
    return ''.join(restored)

def get_nouns(line):
    line_text = nlp(line)
    nouns = []
    for entity in line_text.ents:
        if entity.label_ in ["PERSON", "ORG", "GPE", "FAC", "LOC", "PRODUCT", "EVENT"] :
            nouns.append(entity.text)
    return sorted(nouns)

test_cases = [
    "In April 2023, Sundar Pichai did announce that Google would be launehing a new AI product namcd Gemini. Barack Obama also gave a speech at Harvard University, cmphasizing the role of technology in modern education.",
    "Project X is an exclusive elub at Veermata Jijabai Technological Institute, Mumbai, mcant to 5erve as a healthy environment for 5tudents to learn from each other and grow together. Through the guidance of their mcntors these 5tudents are able to complete daunting tasks.",
    "I will be eompleting my BTech dcgree in Mechanical Engineering from VJTI in 2028",
    "However the rcsults were clear"
]
i = 0
pattern = r'\b(However)\b(?![\w,.;:!?])'
def get_comma(text):
	return re.sub(pattern,r'\1,',text)
for test_case in test_cases:
    print(f"\nTestCase = {i + 1}")
    restored = restore_sentence(test_case)
    nouns = get_nouns(restored)
    final = get_comma(restored)
    print("corrected=", final)
    print("nouns=", nouns)
    i=i+1
