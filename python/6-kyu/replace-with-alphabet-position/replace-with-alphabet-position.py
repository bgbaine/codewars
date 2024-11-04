def alphabet_position(text):
    word = []
    for char in text.lower():
        if char.isalpha():
            word.append(str(ord(char) - 96))
    return " ".join(word)
