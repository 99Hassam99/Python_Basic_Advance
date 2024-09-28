# Write a program to create a dictionary of Urdu words with values as their English translation.
# Provide user with an option to look it up!

urdu_words={
    "Neendh":"Sleep",
    "Hasna":"Laugh",
    "Rona":"Cry",
    "Khafa":"Sad"
            }
word=input("Enter the word you want to translate: ")
print(urdu_words[word])
print(urdu_words.keys())
print(urdu_words.values())