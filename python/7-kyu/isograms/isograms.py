# "Dermatoglyphics" --> true
# "aba" --> false
# "moOse" --> false (ignore letter case)


def is_isogram(str):
    str = str.lower()
    for i, char in enumerate(str[0:]):
        for charD in str[:i]:
            if char == charD:
                return False
    return True
