
# Exercises 5.1

# 1
def subtract(list1, list2):
    event = []
    for i in list1:
        if i not in list2:
            event.append(i)
    return event

def subtract(list1, list2):
    return [item for item in list1 if item not in list2]


def subtract(lst1, lst2):
    return set(lst1) - (set(lst2))


lst1 = ['ani', 'pse','po']
lst2 = ['ani', 'pse',' jo']

# print(subtract(lst1, lst2))  # ['po']

lst3 = ['ose', 'pse', 'po']
lst4 = ['ani', 'pse',' jo']

# print(subtract(lst3, lst4))  # ['ose', 'po']

# 2

def has_duplicates(lst):
    new_list = []
    for item in lst:
        if item in new_list:
            return True
        else:
            new_list.append(item)
    return False


def has_duplicates(lst):
    return len(set(lst)) < len(lst)


lst1 = ['po', 'jo', 'jo']
lst2 = ['ani', 'pse']

# print(has_duplicates(lst1))  # True
# print(has_duplicates(lst2))  # False


# 3

def uses_only(word, available):
    for letter in word:
        if letter not in available:
            return False
    return True


def uses_only(word, available):
    return set(word) <= set(available)


# print(uses_only('ani', 'ano'))  # False
# print(uses_only('an', 'ano'))  # True
# print(uses_only('pse', 'anispe'))  # True
# print(uses_only('po', 'anispe'))  # False
# print(uses_only('anipse', 'pse'))  # False

def avoids(word, forbidden):
    return set(word).isdisjoint(set(forbidden))


# print(avoids('ani', 'po'))  # True
# print(avoids('ani', 'jon'))  # False
# print(avoids('po', 'po'))  # False
# print(avoids('bre', 'a'))  # True
