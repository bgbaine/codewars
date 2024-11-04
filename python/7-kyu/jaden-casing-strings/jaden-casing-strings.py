def to_jaden_case(string):
    words = string.split(" ")
    jaden_str = ""
    for i, word in enumerate(words, 0):
        jaden_str += f"{word.capitalize()}"
        if i != len(words) - 1:
            jaden_str += " "
    return jaden_str
