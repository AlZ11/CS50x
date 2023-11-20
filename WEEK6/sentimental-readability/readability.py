# TODO
from cs50 import get_string

txt = get_string("Text: ")
letters, words, sentences = 0, 1, 0

for i in txt:
    if i.isalpha():
        letters += 1
    elif i == " ":
        words += 1
    elif i == '.' or i == '!' or i == '?':
        sentences += 1
idx = 0.0588 * (letters/words * 100) - 0.296 * (sentences/words * 100) - 15.8

if idx < 1:
    print("Before Grade 1")
elif idx >= 16:
    print("Grade 16+")
else:
    print(f"Grade {round(idx)}")
