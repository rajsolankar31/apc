from texttools.cleaning import remove_punctuation, remove_extra_spaces
from texttools.tokenization import tokenize
from texttools.frequency import word_frequency
text = input("Enter text: ")
clean = remove_extra_spaces(remove_punctuation(text))
print("Cleaned:", clean); tokens = tokenize(clean)
print("Tokens:", tokens); print("Frequency:", word_frequency(tokens))
