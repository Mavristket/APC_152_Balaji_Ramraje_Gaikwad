import string
def remove_punctuation(s): return s.translate(str.maketrans("","",string.punctuation))
def extra_spaces(s): return " ".join(s.split())
