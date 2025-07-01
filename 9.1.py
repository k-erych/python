import string
def popular_words (text = str, words = list):
    a = text.lower()
    for i in string.punctuation:
        a = a.replace(i, "")
    a = a.split() # ['when', 'i', 'was', 'one', 'i', 'had', 'just', 'begun', 'when', 'i', 'was', 'two', 'i', 'was', 'nearly', 'new']
    dict_1 = dict()
    for i in words:
        dict_1[i] = a.count(i)
    return dict_1
text_1 = '''When I was One I had just begun When I was,, Two I was nearly new '''
words_1 = ['i', 'was', 'three', 'near']
print(popular_words(text_1, words_1))