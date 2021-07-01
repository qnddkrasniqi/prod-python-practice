def number(a):
    if a == 1:
        return 'Yes'
    else:
        return 'No'


def number(a):
    return True if a == 1 else False


def my_list(lst):
    if len(lst) > 3:
        return 'Too long'
    else:
        return 'Okay'


def my_list(lst):
    return 'Too long' if len(lst) > 3 else 'Okay'


def numrat(c):
    if c > 0:
        x = 'positive'
    else:
        x = 'negative'
    return x


def numrat(c):
     x = 'positive' if c > 0 else 'negative'
     return x


def is_python(s):
    return 'It is Python' if s == 'Python' else 'It is not Python'


def is_dog(m):
    a = 'Yes' if 'dog' in m else 'No'
    return a


print(is_dog(['dog', 'ali', 4]))
print(is_dog(['ali', 4]))
