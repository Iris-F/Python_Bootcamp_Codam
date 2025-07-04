#!/usr/bin/env python3

word = input("Enter a string:\n")
i = 0
new_word = ""

while i < len(word):
    if word[i].isupper():
        new_word += word[i].lower()
    else:
        new_word += word[i].upper()
    i += 1
print(new_word)