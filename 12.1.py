import codecs
def delete_html_tags(html_file, result_file='cleaned.txt'):
    with open(html_file, "r", encoding="utf-8") as file:
        content = file.read()
    result = ""
    inside_tag = False
    for char in content:
        if char == '<':
            inside_tag = True
        elif char == '>':
            inside_tag = False
            continue
        elif not inside_tag:
            result += char
    with open(result_file, 'w', encoding='utf-8') as file:
        result_file = file.write(result)
        print(result)
delete_html_tags("C:/Users/kzabi/Downloads/draft.html", result_file='cleaned.txt')