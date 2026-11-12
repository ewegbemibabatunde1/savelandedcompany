with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('corridor-insights')
print('corridor-insights at', idx)
print(text[idx-50:idx+600])

