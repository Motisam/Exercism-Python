def abbreviate(words):
    names = words.replace('_','').replace('-',' ').upper().split()
    acronym = []
    for name in names:
        acronym.append(name[0])
    return ''.join(acronym)