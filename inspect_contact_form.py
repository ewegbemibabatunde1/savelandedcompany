with open('contact.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('window.location.href = "mailto:')
if idx != -1:
    print(text[idx-400:idx+300])
else:
    print("Not found")

