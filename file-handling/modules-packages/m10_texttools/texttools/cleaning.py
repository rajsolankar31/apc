import string
def remove_punctuation(t): return t.translate(str.maketrans("", "", string.punctuation))
def remove_extra_spaces(t): return " ".join(t.split())
