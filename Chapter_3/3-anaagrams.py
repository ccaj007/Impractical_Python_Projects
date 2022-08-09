import sys
import load_dictionary

word_list = load_dictionary.load('2of4brif.txt')
anagrams = []

#word = input("enter a word: ")
inp = 'foster'
inp = inp.lower()

for word in word_list:
    if word != inp:
        if sorted(word) == sorted(inp):
            anagrams.append(word)
if len(anagrams) == 0:
    print("no anagrams found")
else:
    print("Anagrams = ", *anagrams, sep='\n')

