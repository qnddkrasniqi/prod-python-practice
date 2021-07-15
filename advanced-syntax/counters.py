import collections

# Exercises 6.1

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)


def is_anagram(s1, s2):
    return collections.Counter(s1) == collections.Counter(s2)


print(is_anagram('iceman', 'cinema'))  # True
print(is_anagram('buba', 'ubab'))  # True
print(is_anagram('pse','ani'))  # False
print(is_anagram('pse','psse'))  # False
print(is_anagram('psse','psee'))  # False
print(is_anagram('ani','ami'))  # False