import string
text_1 = str("  ,, ahhhha'sds")
def first_word(text):
    new_text = text
    while new_text[0] in string.punctuation or new_text[0] == " ":
        new_text = new_text[1:]
    new_string = string.punctuation.replace("'", "")
    i = 0
    true_text = ""
    while i < len(new_text):
        if new_text[i] not in new_string and new_text[i] != " ":
            true_text = true_text + new_text[i]
        else:
            break
        i += 1
    return true_text
print(first_word(text_1))
