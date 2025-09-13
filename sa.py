import string
messages = [
    "Hello world!",
    "Hello, how are you?",
    "World of Python. Hello again.",
    "Python is great, great world."
]
words = []
for message in messages:
    for char in message:
        if char in string.punctuation:
             message = message.replace(char, "")
    message = message.upper()
    splited_message = message.split(" ")
    words.append(splited_message)
corrected_words = []
for lists_of_words in words:
    for word in lists_of_words:
        corrected_words.append(word)
dict_of_quantity_of_words = {}
for word in corrected_words:
    quantity = (corrected_words.count(word))
    dict_of_quantity_of_words[word] = quantity
list_of_sorted = list(sorted(dict_of_quantity_of_words.items(), key=lambda item: item[1]))
print(list_of_sorted[-1][0].capitalize())
print(list_of_sorted[-2][0].capitalize())
print(list_of_sorted[-3][0].capitalize())










