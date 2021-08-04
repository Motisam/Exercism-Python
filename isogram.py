def is_isogram(string):
    chars = string.replace(' ','').replace('-','').lower()
    return len(chars) == len(set(chars))
