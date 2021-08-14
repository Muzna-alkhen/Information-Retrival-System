dictionary = {
    'u.s': 'usa',
    'u.n': 'un',
    'united states': 'usa',
    'united nations': 'un',
    'los angeles' : 'la',
    'viet nam' : 'vietnam',
        }

def dictionaryFormat(s):
    for i in dictionary:
        s = s.replace(i,dictionary[i])
    return s

