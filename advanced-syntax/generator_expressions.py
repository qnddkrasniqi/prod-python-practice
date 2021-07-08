def avoids(word, forbidden):
    for i in word:
        if i in forbidden:
            return False
    return True


def avoids(word, forbidden):
    return not any(i in forbidden for i in word)


def uses_all(word, required):
    for i in required:
        if i not in word:
            return False
    return True


def uses_all(word, required):
    return all(i in word for i in required)


print(uses_all('ani', 'a'))  # True
print(uses_all('buka', 'uka'))  # True
print(uses_all('ali', 'aliu'))  # False
