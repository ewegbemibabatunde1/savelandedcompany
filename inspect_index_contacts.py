with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('Star: <a')
print(text[idx-100:idx+400])

