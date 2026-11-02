from texttools.cleaning import *
from texttools.tokenization import tokenize
from texttools.frequency import word_frequency
s=input("Enter text: "); s=extra_spaces(remove_punctuation(s)); words=tokenize(s)
print("Clean text =",s); print("Tokens =",words); print("Frequency =",word_frequency(words))
